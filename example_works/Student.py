"""
a constructor that takes the student's name and settings
conf = {
'exam_max': 30, # 
the number of points available for passing the exam
'lab_max': 7, # the number of points available for 1 practical work
'lab_num': 10, # number of practical works in the course
'k': 0.61, # the share of points from the maximum that must be scored to obtain a certificate


method make_lab (m, n), which takes 2 arguments 
m - the number of points scored for the task and 
n - the ordinal number of the task (labs are numbered from 0 to lab_num-1).
When re-submitting the task, the last grade is credited. If n is not specified, 
it means the delivery of the first uncompleted practical task.

method make_exam (m), which takes 1 argument score for the final exam

the is_certified () method, which returns a dot containing the real number 
(the sum of the student's points for the course) 
and the logical value True or False, depending on whether these points are enough to obtain a certificate.

"""
class Student():
    def __init__(self, name='', conf = {}, labs=[0], exam=0):
        self.name=name
        self.conf=conf
        for i in range((self.conf['lab_num']-1)):
            labs.append(0)
        self.labs=labs
        self.exam=exam

    def make_lab(self, m=0, n=None):
        if m>self.conf['lab_max']:
            m=self.conf['lab_max']
        if n==None:
            n=self.labs.index(0)
        if n>(self.conf['lab_num']-1):
            return (self)
        self.labs[n]=m
        return (self)

    def make_exam(self, m):
        if m >self.conf['exam_max']:
            m=self.conf['exam_max']
        self.exam=m
        return self

    def is_certified(self):
        flag=False
        if (sum(self.labs)+self.exam)/100.0>=self.conf['k']:
            flag=True
        return (sum(self.labs)+self.exam, flag)
