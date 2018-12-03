
import csv, copy, sys

course_file = sys.argv[1]

def readable_row(row):

        ### college_must
        if str(row[13]).__contains__('Sport Tourism Hospitality Mgt') or str(row[13]).__contains__(
                'Music & Dance') or str(row[13]).__contains__('Medicine') or str(row[13]).__contains__(
                'Media & Comm') or str(row[13]).__contains__('Liberal Arts') or str(row[13]).__contains__(
                'Engineering') or str(row[13]).__contains__('Education') or str(row[13]).__contains__(
                'College of Public Health') or str(row[13]).__contains__('Business & Mngmnt') or str(
                row[13]).__contains__('Art'):
                return False

        ### degree_must
        if str(row[17]).__contains__('Bachelor of Arts') or str(row[17]).__contains__('Bachelor of Fine Arts') or str(
                row[17]).__contains__('Bachelor of Architecture') or str(row[17]).__contains__(
                'Bach of Sci in Engr Tech'):
                return False

        ### level_must
        if str(row[21]).__contains__('Graduate') or str(row[21]).__contains__('Law') or str(row[21]).__contains__(
                'Post Baccalaureate'):
                return False
        ### level_may_not
        if str(row[22]).__contains__('Undergraduate'):
                return False

        return True


def get_course_list(course_file):

        course_list = []
        name_list = []
        credit_list = []
        attribute_list = []
        course_count = 0
        with open(course_file) as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                row_count = 0
                for row in reader:
                        if row_count > 0 and readable_row(row):
                                course_name = row[0] + row[1]
                                name_list.append(course_name)
                                credit_list.append(float(row[3]))
                                attribute_list.append(row[6])
                                course_count += 1
                        row_count += 1
                course_list.append(name_list)
                course_list.append(credit_list)
                course_list.append(attribute_list)
        return course_list


courses_taken = ["MATH701", "MATH1021", "MATH1022", "MATH1031", "MATH1039"]
courses_taken += ["EES2001", 'CIS3515', 'CIS4515', 'CIS3603']


def has_credit_count(course_list, completed_courses):
        credit_count = 0.0
        for i in range(0, len(completed_courses)):
                credit_index = course_list[0].index(completed_courses[i])
                credit_count += course_list[1][credit_index]
        if credit_count >= 123.0:
                return True
        else:
                return False


def has_core_courses(completed_courses):
        core_courses = ['CIS1001',
                        ['CIS1057', 'CIS1051'],
                        ['CIS1068', 'CIS1968'],
                        ['CIS1166', 'CIS1966'],
                        'CIS2033',
                        'CIS2107',
                        'CIS2166',
                        'CIS2168',
                        'CIS3207',
                        'CIS3296',
                        ['CIS4398', 'CIS4397']]

        for course in core_courses:
                if course.__class__ == str:
                        if not completed_courses.__contains__(course):
                                return False
                if course.__class__ == list:
                        if completed_courses.__contains__(course[0]):
                                pass
                        elif completed_courses.__contains__(course[1]):
                                pass
                        else:
                                return False
        return True


def has_math_courses(completed_courses):
        if completed_courses.__contains__("MATH1041") or completed_courses.__contains__("MATH1941"):
                if completed_courses.__contains__("MATH1042"):
                        return True
                elif completed_courses.__contains__("MATH1942"):
                        return True
        return False


def has_cis_electives(course_list, completed_courses):
        credit_count = 0
        cis_electives = ['CIS3203', 'CIS3211', 'CIS3219', 'CIS3242', 'CIS3308', 'CIS3319', 'CIS3381', 'CIS3515',
                         'CIS3603', 'CIS3605', 'CIS3715', 'CIS4282', 'CIS4305', 'CIS4307', 'CIS4308', 'CIS4319',
                         'CIS4324', 'CIS4331', 'CIS4350', 'CIS4360', 'CIS4382', 'CIS4515', 'CIS4615', 'MATH2101',
                         'MATH2103', 'MATH2043']
        for i in range(0, len(cis_electives)):
                if completed_courses.__contains__(cis_electives[i]):
                        credit_count += course_list[1][i]
        if credit_count >= 15:
                return True
        else:
                return False


def has_lab_sequence(completed_courses):
        if completed_courses.__contains__("BIOL1111") or completed_courses.__contains__("BIOL1911"):
                if completed_courses.__contains__("BIOL2112"):
                        return True
                elif completed_courses.__contains__("BIOL2912"):
                        return True

        if (completed_courses.__contains__("CHEM1031") and completed_courses.__contains__("CHEM1033")) or \
                (completed_courses.__contains__("CHEM1951") and completed_courses.__contains__("CHEM1953")):
                if completed_courses.__contains__("CHEM1032") and completed_courses.__contains__("CHEM1034"):
                        return True
                elif completed_courses.__contains__("CHEM1952") and completed_courses.__contains__("CHEM1954"):
                        return True

        if completed_courses.__contains__("EES2001") and (completed_courses.__contains__("EES2011") or
                                                          completed_courses.__contains__("EES2061")):
                return True

        if completed_courses.__contains__("PHYS1061") or completed_courses.__contains__("PHYS1961") or \
                completed_courses.__contains__("PHYS2021") or completed_courses.__contains__("PHYS2921"):
                if completed_courses.__contains__("PHYS1062"):
                        return True
                elif completed_courses.__contains__("PHYS1962"):
                        return True
                elif completed_courses.__contains__("PHYS2022"):
                        return True
                elif completed_courses.__contains__("PHYS2922"):
                        return True
        return False


def has_gen_eds(course_list, completed_courses):
        attributes = ["'GW'", "'GY'", "'GZ'", "'GA'", "'GB'", "'GD'", "'GG'", "'GU'"]
        for attribute in attributes:
                attribute_complete = False
                for i in range(0, len(course_list[0])):
                        if course_list[2][i].__contains__(attribute) and completed_courses.__contains__(course_list[0][i]):
                                attribute_complete = True
                if not attribute_complete:
                        return False
        return True


# Give this function a list of courses that the student has completed in the same format as courses_taken
# You must change the course_file at the top to the path of you local copy of courses.csv
# It will return a True if the student has graduated and False if requirements are not met
def is_graduated(completed_courses):
        course_list = get_course_list(course_file)

        if (has_credit_count(course_list, completed_courses) and has_core_courses(completed_courses) and
                has_math_courses(completed_courses) and has_cis_electives(course_list, completed_courses) and
                has_lab_sequence(completed_courses) and has_gen_eds(course_list, completed_courses)):
                return True
        else:
                return False



