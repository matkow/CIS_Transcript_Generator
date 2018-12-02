
import csv, copy, sys


input_file = sys.argv[1]
if not str(input_file).__contains__(".csv"):
        input_file = input_file + ".csv"

output_file = sys.argv[2]
if not str(output_file).__contains__(".csv"):
        output_file = output_file + ".csv"

course_file = sys.argv[3]

def readable_row(row):
        ### college_must
        if str(row[13]).__contains__('Sport Tourism Hospitality Mgt') or str(row[13]).__contains__(
                'Music & Dance') or str(row[13]).__contains__('Medicine') or str(row[13]).__contains__(
                'Media & Comm') or str(row[13]).__contains__('Liberal Arts') or str(row[13]).__contains__(
                'Engineering') or str(row[13]).__contains__('Education') or str(row[13]).__contains__(
                'College of Public Health') or str(row[13]).__contains__('Business & Mngmnt') or str(
                row[13]).__contains__('Art'):
                return False

        ### degree_must
        if str(row[17]).__contains__('Bachelor of Arts') or str(row[17]).__contains__('Bachelor of Fine Arts') or str(
                row[17]).__contains__('Bachelor of Architecture') or str(row[17]).__contains__(
                'Bach of Sci in Engr Tech'):
                return False

        ### level_must
        if str(row[21]).__contains__('Graduate') or str(row[21]).__contains__('Law') or str(row[21]).__contains__(
                'Post Baccalaureate'):
                return False
        ### level_may_not
        if str(row[22]).__contains__('Undergraduate'):
                return False

        return True


course_list = []
course_count = 0
with open(course_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        row_count = 0
        for row in reader:
                if row_count > 0:
                        course_name = row[0] + " " + row[1]
                        course_list.append(course_name)
                        course_count += 1
                row_count += 1
        print(course_list)
        print(course_count)

vector_list = []
vector_template = []
for i in range(0, course_count):
        vector_template.append(0)

with open(input_file) as csvfile:
        reader = csv.reader(csvfile)

        current_semester_num = 0
        row_num = 0
        for row in reader:
                print(row_num)
                row_num += 1
                vector = copy.copy(vector_template)
                cell_num = 0
                for cell in row:
                        if cell is "":
                                pass
                        else:
                                cell_num += 1
                                if str.isdigit(cell):
                                        current_semester_num = int(cell)
                                else:
                                        a = 0
                                        while not str(cell[a]).isdigit():
                                                a += 1
                                        cell = cell[:a] + " " + cell[a:]
                                        vector[course_list.index(cell)] = current_semester_num
                vector_list.append(vector)

with open(output_file, 'wb') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(course_list)
        for vector in vector_list:
                print(row_num)
                row_num -= 1
                writer.writerow(vector)
