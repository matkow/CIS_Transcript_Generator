import random
from process_data import process_courses


def add_cs_elective_courses(course_list, is_honors):

        elective_credit_count = 0.0
        elective_taken_list = []
        has_math = False

        process_courses.find_course("CIS4282", course_list).prereqs = \
                process_courses.find_course("CIS3603", course_list).prereqs

        cis_elective_list = []
        cis_elective_list.append(process_courses.find_course("CIS3203", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3211", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3219", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3242", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3308", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3319", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3381", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3515", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3603", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3715", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4282", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4305", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4307", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4308", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4319", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4324", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4331", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4350", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4360", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4382", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4515", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4615", course_list))

        math_elective_list = []
        math_elective_list.append(process_courses.find_course("MATH2101", course_list))
        math_elective_list.append(process_courses.find_course("MATH2103", course_list))
        math_elective_list.append(process_courses.find_course("MATH2043", course_list))

        open_elective_list = cis_elective_list + math_elective_list
        while elective_credit_count < 15.0:

                if has_math:
                        r = random.randint(0, len(open_elective_list) - 1)
                        elective_credit_count += int(open_elective_list[r].credits)
                        if open_elective_list[r].name == "CIS4515" and process_courses.find_course("CIS3515", elective_taken_list) == None:
                                elective_credit_count += int(process_courses.find_course("CIS3515", open_elective_list).credits)
                                elective_taken_list.append(process_courses.pop_course("CIS3515", open_elective_list))
                                r -= 1
                        if open_elective_list[r].name == "CIS4615" and process_courses.find_course("CIS3319", elective_taken_list) == None:
                                elective_credit_count += int(process_courses.find_course("CIS3319", open_elective_list).credits)
                                elective_taken_list.append(process_courses.pop_course("CIS3319", open_elective_list))
                                r -= 1
                        elective_taken_list.append(
                                process_courses.pop_course(open_elective_list.pop(r).name, course_list))

                else:
                        r = random.randint(0, len(open_elective_list) - 1)
                        elective_credit_count += int(open_elective_list[r].credits)
                        if math_elective_list.__contains__(open_elective_list[r]):
                                has_math = True
                                elective_taken_list.append(
                                        process_courses.pop_course(open_elective_list[r].name, course_list))
                                for each in math_elective_list:
                                        open_elective_list.remove(each)
                        else:
                                if open_elective_list[r].name == "CIS4515" and process_courses.find_course("CIS3515", elective_taken_list) == None:
                                        elective_credit_count += int(process_courses.find_course("CIS3515", open_elective_list).credits)
                                        elective_taken_list.append(process_courses.pop_course("CIS3515", open_elective_list))
                                        r -= 1
                                if open_elective_list[r].name == "CIS4615" and process_courses.find_course("CIS3319", elective_taken_list) == None:
                                        elective_credit_count += int(process_courses.find_course("CIS3319", open_elective_list).credits)
                                        elective_taken_list.append(process_courses.pop_course("CIS3319", open_elective_list))
                                        r -= 1
                                elective_taken_list.append(
                                        process_courses.pop_course(open_elective_list.pop(r).name, course_list))

        return elective_taken_list


def add_isnt_elective_courses(course_list, is_honors):

        elective_credit_count = 0.0
        elective_taken_list = []
        has_math = False

        process_courses.find_course("CIS4282", course_list).prereqs = \
                process_courses.find_course("CIS3603", course_list).prereqs

        cis_elective_list = []
        cis_elective_list.append(process_courses.find_course("CIS3281", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3374", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3376", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3515", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3603", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3605", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3715", course_list))
        cis_elective_list.append(process_courses.find_course("CIS3775", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4105", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4106", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4108", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4282", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4330", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4340", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4344", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4350", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4362", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4376", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4378", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4515", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4615", course_list))
        cis_elective_list.append(process_courses.find_course("CIS4625", course_list))

        while elective_credit_count < 12.0:

                r = random.randint(0, len(cis_elective_list) - 1)
                elective_credit_count += int(cis_elective_list[r].credits)
                if cis_elective_list[r].name == "CIS3715" and process_courses.find_course("CIS2166", elective_taken_list) == None:
                        if is_honors:
                                if process_courses.find_course("MATH1941", course_list) != None:
                                        elective_credit_count += int(
                                                process_courses.find_course("MATH1941", course_list).credits)
                                        elective_taken_list.append(process_courses.pop_course("MATH1941", course_list))
                        else:
                                if process_courses.find_course("MATH1041", course_list) != None:
                                        elective_credit_count += int(
                                                process_courses.find_course("MATH1041", course_list).credits)
                                        elective_taken_list.append(process_courses.pop_course("MATH1041", course_list))
                        elective_credit_count += int(process_courses.find_course("CIS2166", course_list).credits)
                        elective_taken_list.append(process_courses.pop_course("CIS2166", course_list))
                        r -= 0
                if cis_elective_list[r].name == "CIS4515" and process_courses.find_course("CIS3515", elective_taken_list) == None:
                        elective_credit_count += int(process_courses.find_course("CIS3515", cis_elective_list).credits)
                        elective_taken_list.append(process_courses.pop_course("CIS3515", cis_elective_list))
                        r -= 1
                if cis_elective_list[r].name == "CIS4615" and process_courses.find_course("CIS3319", elective_taken_list) == None:
                        elective_credit_count += int(process_courses.find_course("CIS2107", course_list).credits)
                        elective_taken_list.append(process_courses.pop_course("CIS2107", course_list))
                        elective_credit_count += int(process_courses.find_course("CIS3319", course_list).credits)
                        elective_taken_list.append(process_courses.pop_course("CIS3319", course_list))
                        r -= 0
                if cis_elective_list[r].name == "CIS4625" and process_courses.find_course("CIS4378", elective_taken_list) == None:
                        elective_credit_count += int(process_courses.find_course("CIS4378", cis_elective_list).credits)
                        elective_taken_list.append(process_courses.pop_course("CIS4378", cis_elective_list))
                        r -= 1
                elective_taken_list.append(
                        process_courses.pop_course(cis_elective_list.pop(r).name, course_list))

        return elective_taken_list
