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
