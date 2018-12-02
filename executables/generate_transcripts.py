import sys, copy, csv, random, time
from classes.Student import Student
from classes.Semester import Semester
from process_data import process_courses, process_prerequisites
from util import draw_num, probability


def transcript_by_semester_to_csv(output_file, transcript_list, print_out):
        if not str(output_file).__contains__(".csv"):
                output_file = output_file + ".csv"

        with open(output_file, 'a') as csvfile:
                writer = csv.writer(csvfile)
                for transcript in transcript_list:
                        i = 1
                        row = []
                        for semester in transcript:
                                row.append(i)
                                for course in semester:
                                        row.append(course)
                                i += 1
                        if print_out:
                                print(row)
                        writer.writerow(row)


major = sys.argv[1]
num_of_transcripts = int(sys.argv[2])
i_range = 100
n_range = int(num_of_transcripts/i_range)
transcripts_sum = 0

course_list = process_courses.create_courses(sys.argv[3])
output_file = sys.argv[4]



for n in range(0, n_range):
        transcript_list = []

        for i in range(0, i_range):

                t0 = time.process_time()

                if random.random() > probability.honors:
                        is_honors = False
                else:
                        is_honors = True
                local_course_list = copy.copy(course_list)
                student = Student(major, local_course_list, is_honors)

                completed_courses = copy.copy(student.completed_courses)
                classes_taken = ["MATH0701", "MATH1021", "MATH1022", "MATH1031", "MATH1039"]
                semester_list = []
                while len(student.completed_courses) > 0:
                        semester = Semester()
                        while semester.credit_count < 16 and len(semester.courses) < 5 and (len(student.completed_courses)) > 0:
                                r = random.randint(0, len(student.completed_courses) - 1)
                                if process_prerequisites.are_prereqs_satisfied(classes_taken, student.completed_courses[r].prereqs):
                                        classes_taken.append(student.completed_courses[r].name)
                                        semester.courses.append(student.completed_courses.pop(r))
                                else:
                                        if time.process_time() - t0 > 3.0:
                                                print("Remaining Courses: ")
                                                for course in student.completed_courses:
                                                        print("   " + course.name + "  " + str(course.prereqs))
                                                print
                                                print("Taken Courses: ")
                                                for course in classes_taken:
                                                        print("   " + course)
                                                exit()
                        semester_list.append(semester)
                        print("    " + str(len(student.completed_courses)))

                        transcript_semester = []
                        current_semester = 0
                        last_semester = random.randint(0, 10)
                for semester in semester_list:
                        if current_semester > last_semester:
                                break
                        else:
                                current_semester += 1
                        courses = []
                        for course in semester.courses:
                                courses.append(copy.copy(course.name))
                        transcript_semester.append(courses)
                        print(courses)
                print(len(transcript_semester))
                print(i)
                transcript_list.append(transcript_semester)

        for transcript in transcript_list:
                transcripts_sum += 1

        transcript_by_semester_to_csv(output_file, transcript_list, True)
        print(draw_num.print_num(transcripts_sum))

