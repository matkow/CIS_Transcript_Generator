
def credit_count(df, x):
        credit_count = 0
        for i in range(0, len(df.values[0])):
                credit_count += df.values[x][i]
                # print(df.columns[i] + " " + str(df.values[x][i]))
        if credit_count < 123:
                return False
        return True


def core_course(df, x):
        core_courses = ['CIS 1001',
                        ['CIS 1057', 'CIS 1051'],
                        ['CIS 1068', 'CIS 1968'],
                        ['CIS 1166', 'CIS 1966'],
                        'CIS 2033',
                        'CIS 2107',
                        'CIS 2166',
                        'CIS 2168',
                        'CIS 3207',
                        'CIS 3296',
                        ['CIS 4398', 'CIS 4397']]

        for course in core_courses:
                if course.__class__ == str:
                        if df[course][x] == 0:
                                return False
                        # print(course + "  " + str(df[course][x]))
                if course.__class__ == list:
                        if df[course[0]][x] > 0:
                                # print(course[0] + "  " + str(df[course[0]][x]))
                                pass
                        elif df[course[1]][x] > 0:
                                # print(course[1] + "  " + str(df[course[1]][x]))
                                pass
                        else:
                                return False
        return True


def math_courses(df, x):

        if df['MATH 1041'][x] == 0 and df['MATH 1941'][x] == 0:
                return False
        # print('MATH 1041')
        if df['MATH 1042'][x] == 0 and df['MATH 1942'][x] == 0:
                return False
        # print('MATH 1042')

        return True


def cis_electives(df, x, course_list):

        cis_electives = ['CIS 3203', 'CIS 3211', 'CIS 3219', 'CIS 3242', 'CIS 3308', 'CIS 3319', 'CIS 3381', 'CIS 3515',
                         'CIS 3603', 'CIS 3605', 'CIS 3715', 'CIS 4282', 'CIS 4305', 'CIS 4307', 'CIS 4308', 'CIS 4319',
                         'CIS 4324', 'CIS 4331', 'CIS 4350', 'CIS 4360', 'CIS 4382', 'CIS 4515', 'CIS 4615', 'MATH 2101',
                         'MATH 2103', 'MATH 2043']

        credit_count = 0
        for course in cis_electives:
                if df[course][x] > 0:
                        credit_count += course_list[course_list.index(course) + 1]

        if credit_count < 15:
                return False
        else:
                return True


def lab_science_sequence(df, x):

        if df['BIOL 1111'][x] > 0 and df['BIOL 2112'][x] > 0:
                return True
        if df['BIOL 1911'][x] > 0 and df['BIOL 2912'][x] > 0:
                return True

        if df['CHEM 1031'][x] > 0 and df['CHEM 1033'][x] > 0 and df['CHEM 1032'][x] and df['CHEM 1034'][x]:
                return True
        if df['CHEM 1951'][x] > 0 and df['CHEM 1953'][x] > 0 and df['CHEM 1952'][x] and df['CHEM 1954'][x]:
                return True

        if df['EES 2001'][x] > 0 and df['EES 2011'][x] > 0:
                return True
        if df['BIOL 2001'][x] > 0 and df['EES 2061'][x] > 0:
                return True

        if df['PHYS 1061'][x] > 0 and df['PHYS 1062'][x] > 0:
                return True
        if df['PHYS 1961'][x] > 0 and df['PHYS 1962'][x] > 0:
                return True
        if df['PHYS 2021'][x] > 0 and df['PHYS 2022'][x] > 0:
                return True
        if df['PHYS 2921'][x] > 0 and df['PHYS 2922'][x] > 0:
                return True

        return False


def geneds(df, x, course_list):

        attributes = ["GW", "GY", "GZ", "GA", "GB", "GD", "GG", "GU"]
        for attribute in attributes:
                i = 2
                current_attribute_complete = False
                while i < len(course_list):
                        if str(course_list[i]).find(attribute) > 0:
                                if df[course_list[i - 2]][x] > 0:
                                        current_attribute_complete = True
                                        # print(course_list[i - 2])
                        i += 3
                if not current_attribute_complete:
                        return False

        return True
