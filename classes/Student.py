from requirements import requirements_math, requirements_free_electives, requirements_geneds, \
        requirements_lab_science, requirements_cis_electives, requirements_core


class Student:

        def __init__(self, major, course_list, is_honors):

                self.major = major
                self.course_list = course_list
                self.is_honors = is_honors
                self.completed_courses = self.add_courses(major, course_list, is_honors)
                self.credit_count = self.sum_credit_count(self.completed_courses)

        def print_completed_courses(self):
                i = 0
                n = 0
                for course in self.completed_courses:
                        i += 1
                        n += course.credits
                        print (str(i).ljust(4) + course.name + ":").ljust(15) + course.title

                print("Number of Credits: " + str(n))
                print("Number of Classes: " + str(len(self.completed_courses)))


        def sum_credit_count(self, completed_courses):

                credit_count = 0
                for course in completed_courses:
                        credit_count += course.credits

                return credit_count


        def add_courses(self, major, course_list, is_honors):

                if major == 'CS':
                        return self.add_CS_courses(course_list, is_honors)
                if major == 'ISNT':
                        return self.add_ISNT_courses(course_list, is_honors)
                else:
                        return None

        def add_CS_courses(self, course_list, is_honors):

                completed_courses = []
                completed_courses += requirements_core.add_cs_core_courses(course_list, is_honors)
                completed_courses += requirements_math.add_cs_math_courses(course_list, is_honors)
                completed_courses += requirements_cis_electives.add_cs_elective_courses(course_list, is_honors)
                completed_courses += requirements_lab_science.add_cs_lab_science_courses(course_list, is_honors)
                completed_courses += requirements_geneds.add_geneds(course_list, is_honors)
                credit_count = self.sum_credit_count(completed_courses)
                completed_courses += requirements_free_electives.add_free_electives(completed_courses, course_list, is_honors, credit_count)

                return completed_courses


        def add_ISNT_courses(self, course_list, is_honors):

                completed_courses = []
                completed_courses += requirements_core.add_isnt_core_courses(course_list, is_honors)
                completed_courses += requirements_math.add_isnt_math_courses(course_list, is_honors)
                completed_courses += requirements_cis_electives.add_isnt_elective_courses(course_list, is_honors)
                completed_courses += requirements_lab_science.add_isnt_lab_science_courses(course_list, is_honors)
                completed_courses += requirements_geneds.add_geneds(course_list, is_honors)
                credit_count = self.sum_credit_count(completed_courses)
                completed_courses += requirements_free_electives.add_free_electives(completed_courses, course_list,
                                                                                    is_honors, credit_count)

                return completed_courses



