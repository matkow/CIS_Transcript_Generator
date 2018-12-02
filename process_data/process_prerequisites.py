
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
