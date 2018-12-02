import subprocess, threading

number_of_transcripts = str(30000)
gen_transcripts = 'C:\\Users\Matthew\PycharmProjects\Major_ComputerScienceGenerator\executables\generate_transcripts.py'
gen_vector = 'C:\\Users\Matthew\PycharmProjects\Major_ComputerScienceGenerator\executables\\transcripts_to_vector.py'
courses_file = 'C:\\Users\Matthew\PycharmProjects\Major_ComputerScienceGenerator\data_files\courses.csv'

cs_major = 'CS'
cs_transcript_file = 'C:\\Users\Matthew\PycharmProjects\Major_ComputerScienceGenerator\data_files\\transcript\\transcripts_cs_partials_v2.csv'
cs_vector_file = 'C:\\Users\Matthew\PycharmProjects\Major_ComputerScienceGenerator\data_files\\vector\\vector_cs_partials_v2.csv'

isnt_major = 'ISNT'
isnt_transcript_file = 'C:\\Users\Matthew\PycharmProjects\Major_ComputerScienceGenerator\data_files\\transcript\\transcripts_isnt_partials_v2.csv'
isnt_vector_file = 'C:\\Users\Matthew\PycharmProjects\Major_ComputerScienceGenerator\data_files\\vector\\vector_isnt_partials_v2.csv'


class CS_Gen(threading.Thread):
        def __init__(self):
                self.stdout = None
                self.stderr = None
                threading.Thread.__init__(self)

        def run(self):
                cs_code = subprocess.run(
                        ['python', gen_transcripts, cs_major, number_of_transcripts, courses_file, cs_transcript_file])
                if cs_code == 0:
                        subprocess.run(['python', gen_vector, cs_transcript_file, cs_vector_file])


class ISNT_Gen(threading.Thread):
        def __init__(self):
                self.stdout = None
                self.stderr = None
                threading.Thread.__init__(self)

        def run(self):
                isnt_code = subprocess.run(['python', gen_transcripts, isnt_major, number_of_transcripts, courses_file,
                                            isnt_transcript_file])
                if isnt_code == 0:
                        subprocess.run(['python', gen_vector, isnt_transcript_file, isnt_vector_file])


CS_Gen().start()
ISNT_Gen().start()




