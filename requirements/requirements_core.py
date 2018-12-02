import random
from process_data import process_courses
from util import probability


def add_cs_core_courses(course_list, is_honors):

        core_course_list = []

        core_course_list.append(process_courses.pop_course("CIS1001", course_list))

        # Roughly even split of classes offered between 1057 and 1051
        if random.random() > .5:
                core_course_list.append(process_courses.pop_course("CIS1051", course_list))
        else:
                core_course_list.append(process_courses.pop_course("CIS1057", course_list))

        if is_honors:
                core_course_list.append(process_courses.pop_course("CIS1968", course_list))
        else:
                core_course_list.append(process_courses.pop_course("CIS1068", course_list))

        if is_honors:
                core_course_list.append(process_courses.pop_course("CIS1966", course_list))
        else:
                core_course_list.append(process_courses.pop_course("CIS1166", course_list))

        core_course_list.append(process_courses.pop_course("CIS2033", course_list))
        core_course_list.append(process_courses.pop_course("CIS2107", course_list))
        core_course_list.append(process_courses.pop_course("CIS2166", course_list))
        core_course_list.append(process_courses.pop_course("CIS2168", course_list))
        core_course_list.append(process_courses.pop_course("CIS3207", course_list))
        core_course_list.append(process_courses.pop_course("CIS3223", course_list))
        core_course_list.append(process_courses.pop_course("CIS3296", course_list))

        process_courses.find_course("CIS4398", course_list).prereqs[1].append("CIS3296")

        if random.random() > probability.capstone:
                core_course_list.append(process_courses.pop_course("CIS4398", course_list))
        else:
                process_courses.find_course("CIS4397", course_list).prereqs = \
                        process_courses.find_course("CIS4398", course_list).prereqs
                core_course_list.append(process_courses.pop_course("CIS4397", course_list))

        return core_course_list

def add_isnt_core_courses(course_list, is_honors):

        core_course_list = []

        core_course_list.append(process_courses.pop_course("CIS1001", course_list))

        # Roughly even split of classes offered between 1057 and 1051
        if random.random() > .5:
                core_course_list.append(process_courses.pop_course("CIS1051", course_list))
        else:
                core_course_list.append(process_courses.pop_course("CIS1057", course_list))

        if is_honors:
                core_course_list.append(process_courses.pop_course("CIS1968", course_list))
        else:
                core_course_list.append(process_courses.pop_course("CIS1068", course_list))

        if is_honors:
                core_course_list.append(process_courses.pop_course("CIS1966", course_list))
        else:
                core_course_list.append(process_courses.pop_course("CIS1166", course_list))

        core_course_list.append(process_courses.pop_course("CIS2109", course_list))
        core_course_list.append(process_courses.pop_course("CIS2168", course_list))
        core_course_list.append(process_courses.pop_course("CIS2229", course_list))
        core_course_list.append(process_courses.pop_course("CIS3309", course_list))
        core_course_list.append(process_courses.pop_course("CIS3329", course_list))
        core_course_list.append(process_courses.pop_course("CIS3342", course_list))
        core_course_list.append(process_courses.pop_course("CIS3344", course_list))
        core_course_list.append(process_courses.pop_course("CIS4296", course_list))
        core_course_list.append(process_courses.pop_course("CIS4396", course_list))

        return core_course_list
