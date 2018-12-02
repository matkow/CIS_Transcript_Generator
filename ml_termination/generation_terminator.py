import pandas, sys
import ml_termination.check_functions as check


def format_file(filename):
        if not str(filename).__contains__(".csv"):
                filename = filename + ".csv"
        return filename


def create_course_list(filename):

        format_file(filename)
        dataframe = pandas.read_csv(filename)
        courses = []

        for i in range(0, (len(df.index))):

                course_name = dataframe.at[i, 'subject_code'] + " " + str(dataframe.at[i, 'course_number'])
                course_credits = int(dataframe.at[i, 'number_of_credits'])
                course_attributes = dataframe.at[i, 'attributes']
                courses.append(course_name)
                courses.append(course_credits)
                courses.append(course_attributes)

        return courses


def can_graduate():
        if (check.credit_count(df, x) and check.core_course(df, x) and check.math_courses(df, x)
                and check.cis_electives(df, x) and check.lab_science_sequence(df, x) and check.geneds(df, x)):
                return True
        else:
                return False


courses_file = format_file(sys.argv[1])
course_list = create_course_list(courses_file)

vector_file = format_file(sys.argv[2])
df = pandas.read_csv(vector_file)

can_graduate = False
x = 0

print("Credits " + str(check.credit_count(df, x)))
print("Core Courses " + str(check.core_course(df, x)))
print("Math Courses " + str(check.math_courses(df, x)))
print("CIS Electives " + str(check.cis_electives(df, x, course_list)))
print("Science Sequence " + str(check.lab_science_sequence(df, x)))
print("GenEds " + str(check.geneds(df, x, course_list)))
