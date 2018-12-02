from classes.Course import Course
from process_data import process_attributes, process_prerequisites


def inital_clean(courses):
        for course in courses:
                s_reqs = str(course.prereqs)
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
                course.prereqs = s_reqs
        return courses

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


def create_courses(courses_file):

        import csv
        if not str(courses_file).__contains__(".csv"):
                courses_file = courses_file + ".csv"

        with open(courses_file) as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                cell_count = 0
                course_list = []
                for row in reader:
                        if cell_count > 0 and readable_row(row):
                                course_list.append(Course(
                                        cell_count, row[0], row[1], row[2], float(row[3]), row[7], row[6]))
                        cell_count += 1
        course_list = inital_clean(course_list)
        i = 0
        for course in course_list:
                course.prereqs = process_prerequisites.create_reqs_list(course.prereqs)
                course.attributes = process_attributes.create_attr_list(course.attributes)
        return course_list


def find_course(name, courses):
        for course in courses:
                if course.name == name:
                        return course
        return None


def pop_course(name, courses):
        i = courses.index(find_course(name, courses))
        return courses.pop(i)


