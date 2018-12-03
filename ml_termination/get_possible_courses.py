
import csv, copy, sys

course_file = sys.argv[1]


def clean(prereqs):
        s_reqs = str(prereqs)
        s_reqs = s_reqs.replace(" ", "")
        s_reqs = s_reqs.replace("'", "")
        s_reqs = s_reqs[1:-1]
        if s_reqs != "" and s_reqs[0] == "[":
                s_reqs = s_reqs[1:-1]
        i = 0
        while i < s_reqs.__len__():
                if s_reqs[i] == "[":
                        if s_reqs[i + 1:i + 3] != "OR" and s_reqs[i + 1:i + 4] != "AND":
                                j = s_reqs.find(']', i)
                                temp1 = s_reqs[:j]
                                temp2 = s_reqs[j + 1:]
                                s_reqs = temp1 + temp2
                                temp1 = s_reqs[:i]
                                temp2 = s_reqs[i + 1:]
                                s_reqs = temp1 + temp2
                i += 1
        return s_reqs


def reqs_string_to_list(s_reqs):
        reqs = []
        while s_reqs.__contains__(','):
                if s_reqs[0] == '[':
                        i = 1
                        c = 1
                        while i < s_reqs.__len__():
                                if s_reqs[i] == '[':
                                        c += 1
                                if s_reqs[i] == ']':
                                        c -= 1
                                if c == 0:
                                        reqs.append(reqs_string_to_list(s_reqs[1:i + 0]))
                                        s_reqs = s_reqs[i + 2:]
                                        break
                                i += 1
                else:
                        reqs.append(s_reqs[:s_reqs.find(',')])
                        s_reqs = s_reqs[s_reqs.find(',') + 1:]
        reqs.append(s_reqs)
        return reqs


def create_reqs_list(prereqs):

        s_reqs = str(prereqs)
        reqs = reqs_string_to_list(s_reqs)
        prereqs = reqs

        return prereqs


def are_prereqs_satisfied(courses_taken, reqs):

        if type(courses_taken[0]) != str:
                input_courses = []
                for course in courses_taken:
                        input_courses.append(course.name)
                courses_taken = input_courses

        i = 0
        if reqs[i] == '':
                return True
        if reqs[i] != "AND" and reqs[i] != "OR":
                return courses_taken.__contains__(reqs[i])

        if reqs[i] == "AND":
                for each in reqs:
                        if i > 0:
                                if type(each) == str:
                                        if not list(courses_taken).__contains__(each) and each != '':
                                                return False
                                if type(each) == list:
                                        if not are_prereqs_satisfied(courses_taken, each):
                                                return False
                        i += 1
                return True

        if reqs[i] == "OR":
                for each in reqs:
                        if i > 0:
                                if type(each) == str:
                                        if list(courses_taken).__contains__(each):
                                                return True
                                if type(each) == list:
                                        if are_prereqs_satisfied(courses_taken, each):
                                                return True
                        i += 1
                return False

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
        prereq_list = []
        course_count = 0
        with open(course_file) as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                row_count = 0
                for row in reader:
                        if row_count > 0 and readable_row(row):
                                course_name = row[0] + row[1]
                                name_list.append(course_name)
                                course_reqs = clean(row[7])
                                course_reqs = create_reqs_list(course_reqs)
                                prereq_list.append(course_reqs)
                                course_count += 1
                        row_count += 1
                course_list.append(name_list)
                course_list.append(prereq_list)

        return course_list


# Give this function a list of courses that the student has completed in the same format as courses_taken
# It will return a list in the same format of all the possible courses the student can take
# You must change the course_file at the top to the path of you local copy of courses.csv
# The courses_taken list has to remain as these are assumed classes
def get_possible_courses(completed_courses):
        courses_taken = ["MATH0701", "MATH1021", "MATH1022", "MATH1031", "MATH1039"]
        courses_taken += completed_courses
        course_list = get_course_list(course_file)
        possible_courses = []

        for i in range(0, len(course_list[0])):
                if are_prereqs_satisfied(courses_taken, course_list[1][i]):
                        possible_courses.append(course_list[0][i])

        return possible_courses
