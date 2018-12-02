import random
from process_data import process_courses


def add_geneds(course_list, is_honors):
        gened_course_list = []
        attributes = ["GW", "GY", "GZ", "GA", "GB", "GD", "GG", "GU"]

        for attribute in attributes:
                matching_course_list = []
                for course in course_list:
                        if is_honors:
                                # if list(course.attributes).__contains__(attribute) and (int(course.number) / 900) == 0:
                                if list(course.attributes).__contains__(attribute):
                                        matching_course_list.append(course)
                        else:
                                if list(course.attributes).__contains__(attribute) and (int(course.number) / 900) != 0:
                                        matching_course_list.append(course)

                selected_course = matching_course_list[random.randint(0, len(matching_course_list) - 1)]
                gened_course_list.append(process_courses.pop_course(selected_course.name, course_list))

        return gened_course_list

