import random
from process_data import process_prerequisites, process_courses


def update_matching_course_list(completed_courses, free_elective_course_list, course_list):
        input_courses = completed_courses + free_elective_course_list
        matching_course_list = []
        for course in course_list:
                if process_prerequisites.are_prereqs_satisfied(input_courses, course.prereqs):
                        matching_course_list.append(course)
        return matching_course_list


def add_free_electives(completed_courses, course_list, is_honors, credit_count):
        free_elective_course_list = []
        while credit_count < 123.0:
                matching_course_list = update_matching_course_list(completed_courses, free_elective_course_list, course_list)
                selected_course = matching_course_list[random.randint(0, len(matching_course_list) - 1)]
                free_elective_course_list.append(process_courses.pop_course(selected_course.name, course_list))
                credit_count += selected_course.credits

        return free_elective_course_list




