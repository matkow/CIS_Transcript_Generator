from process_data import process_courses
import random


def add_cs_math_courses(course_list, is_honors):

        math_course_list = []

        if is_honors:
                math_course_list.append(process_courses.pop_course("MATH1941", course_list))
                math_course_list.append(process_courses.pop_course("MATH1942", course_list))
        else:
                math_course_list.append(process_courses.pop_course("MATH1041", course_list))
                math_course_list.append(process_courses.pop_course("MATH1042", course_list))

        return math_course_list


def add_isnt_math_courses(course_list, is_honors):

        math_course_list = []

        if is_honors:
                math_course_list.append(process_courses.pop_course("MATH1941", course_list))
        else:
                if random.random() > 0.33:
                        math_course_list.append(process_courses.pop_course("MATH1041", course_list))
                else:
                        math_course_list.append(process_courses.pop_course("MATH1031", course_list))

        return math_course_list
