import random
from util import probability
from process_data import process_courses


def add_cs_lab_science_courses(course_list, is_honors):

        lab_science_course_list = []
        r = random.random()

        sequence_probability = probability.biology_sequence
        if r <= sequence_probability:
                if is_honors:
                        lab_science_course_list.append(process_courses.pop_course("CHEM1951", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1952", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM2921", course_list))
                        lab_science_course_list.append(process_courses.pop_course("BIOL1911", course_list))
                        lab_science_course_list.append(process_courses.pop_course("BIOL2912", course_list))
                else:
                        lab_science_course_list.append(process_courses.pop_course("CHEM1031", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1032", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM2211", course_list))
                        lab_science_course_list.append(process_courses.pop_course("BIOL1111", course_list))
                        lab_science_course_list.append(process_courses.pop_course("BIOL2112", course_list))

                return lab_science_course_list

        sequence_probability += probability.chemistry_sequence
        if r <= sequence_probability:
                if is_honors:
                        lab_science_course_list.append(process_courses.pop_course("CHEM1951", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1953", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1952", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1954", course_list))
                else:
                        lab_science_course_list.append(process_courses.pop_course("CHEM1031", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1033", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1032", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1034", course_list))

                return lab_science_course_list

        sequence_probability += probability.ees_sequence
        if r <= sequence_probability:
                lab_science_course_list.append(process_courses.pop_course("EES2001", course_list))

                if is_honors:
                        lab_science_course_list.append(process_courses.pop_course("CHEM1951", course_list))
                else:
                        lab_science_course_list.append(process_courses.pop_course("CHEM1031", course_list))

                if random.random() <= probability.minerology:
                        lab_science_course_list.append(process_courses.pop_course("EES2011", course_list))
                else:
                        lab_science_course_list.append(process_courses.pop_course("EES2061", course_list))

                return lab_science_course_list

        else:
                if random.random() <= probability.classical_physics:
                        if is_honors:
                                lab_science_course_list.append(process_courses.pop_course("PHYS1961", course_list))
                                lab_science_course_list.append(process_courses.pop_course("PHYS1962", course_list))
                        else:
                                lab_science_course_list.append(process_courses.pop_course("PHYS1061", course_list))
                                lab_science_course_list.append(process_courses.pop_course("PHYS1062", course_list))
                else:
                        if is_honors:
                                lab_science_course_list.append(process_courses.pop_course("PHYS2921", course_list))
                                lab_science_course_list.append(process_courses.pop_course("PHYS2922", course_list))
                        else:
                                lab_science_course_list.append(process_courses.pop_course("PHYS2021", course_list))
                                lab_science_course_list.append(process_courses.pop_course("PHYS2022", course_list))

                return lab_science_course_list

def add_isnt_lab_science_courses(course_list, is_honors):

        lab_science_course_list = []
        r = random.random()

        sequence_probability = probability.biology_sequence
        if r <= sequence_probability:
                if is_honors:
                        if course_list.__contains__(process_courses.find_course("MATH1941", course_list)):
                                lab_science_course_list.append(process_courses.pop_course("MATH1941", course_list))
                        if course_list.__contains__(process_courses.find_course("MATH1942", course_list)):
                                lab_science_course_list.append(process_courses.pop_course("MATH1942", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1951", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1952", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM2921", course_list))
                        lab_science_course_list.append(process_courses.pop_course("BIOL1911", course_list))
                        lab_science_course_list.append(process_courses.pop_course("BIOL2912", course_list))
                else:
                        if course_list.__contains__(process_courses.find_course("MATH1041", course_list)):
                                lab_science_course_list.append(process_courses.pop_course("MATH1041", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1031", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1032", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM2211", course_list))
                        lab_science_course_list.append(process_courses.pop_course("BIOL1111", course_list))
                        lab_science_course_list.append(process_courses.pop_course("BIOL2112", course_list))

                return lab_science_course_list

        sequence_probability += probability.chemistry_sequence
        if r <= sequence_probability:
                if is_honors:
                        if course_list.__contains__(process_courses.find_course("MATH1941", course_list)):
                                lab_science_course_list.append(process_courses.pop_course("MATH1941", course_list))
                        if course_list.__contains__(process_courses.find_course("MATH1942", course_list)):
                                lab_science_course_list.append(process_courses.pop_course("MATH1942", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1951", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1953", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1952", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1954", course_list))
                else:
                        if course_list.__contains__(process_courses.find_course("MATH1041", course_list)):
                                lab_science_course_list.append(process_courses.pop_course("MATH1041", course_list))
                        if course_list.__contains__(process_courses.find_course("MATH1042", course_list)):
                                lab_science_course_list.append(process_courses.pop_course("MATH1042", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1031", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1033", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1032", course_list))
                        lab_science_course_list.append(process_courses.pop_course("CHEM1034", course_list))

                return lab_science_course_list

        sequence_probability += probability.ees_sequence
        if r <= sequence_probability:
                lab_science_course_list.append(process_courses.pop_course("EES2001", course_list))

                if is_honors:
                        lab_science_course_list.append(process_courses.pop_course("CHEM1951", course_list))
                else:
                        lab_science_course_list.append(process_courses.pop_course("CHEM1031", course_list))

                if random.random() <= probability.minerology:
                        lab_science_course_list.append(process_courses.pop_course("EES2011", course_list))
                else:
                        lab_science_course_list.append(process_courses.pop_course("EES2061", course_list))

                return lab_science_course_list

        else:
                if is_honors:
                        if course_list.__contains__(process_courses.find_course("MATH1941", course_list)):
                                lab_science_course_list.append(process_courses.pop_course("MATH1941", course_list))
                        lab_science_course_list.append(process_courses.pop_course("MATH1942", course_list))
                else:
                        if course_list.__contains__(process_courses.find_course("MATH1041", course_list)):
                                lab_science_course_list.append(process_courses.pop_course("MATH1041", course_list))
                        lab_science_course_list.append(process_courses.pop_course("MATH1042", course_list))

                if random.random() <= probability.classical_physics:
                        if is_honors:
                                lab_science_course_list.append(process_courses.pop_course("PHYS1961", course_list))
                                lab_science_course_list.append(process_courses.pop_course("PHYS1962", course_list))
                        else:
                                lab_science_course_list.append(process_courses.pop_course("PHYS1061", course_list))
                                lab_science_course_list.append(process_courses.pop_course("PHYS1062", course_list))
                else:
                        if is_honors:
                                lab_science_course_list.append(process_courses.pop_course("PHYS2921", course_list))
                                lab_science_course_list.append(process_courses.pop_course("PHYS2922", course_list))
                        else:
                                lab_science_course_list.append(process_courses.pop_course("PHYS2021", course_list))
                                lab_science_course_list.append(process_courses.pop_course("PHYS2022", course_list))

                return lab_science_course_list