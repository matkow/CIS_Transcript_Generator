class Course:

        def __init__(self, i, subject, number, title, credits, prereqs, attributes):
                self.i = i
                self.subject = subject
                self.number = number
                self.title = title
                self.credits = credits
                self.prereqs = prereqs
                self.attributes = attributes
                self.name = self.subject + str(self.number)


