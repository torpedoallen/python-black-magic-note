# coding=utf8

import time



class A(object):

    __slots__ = ['name1','name2','name3','name4','name5']

    def __init__(self, name):
        self.name1 = name
        self.name2 = name
        self.name3 = name
        self.name4 = name
        self.name5 = name


a = [A(str(i)) for i in xrange(100000)]
print dir(a[0])
time.sleep(10)
