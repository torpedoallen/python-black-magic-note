# coding=utf8

import time

with open('/tmp/a', 'rb') as f:

    def read0():
        print 'start read 0'
        return (r for r in f)


    def read1():
        print 'start read 1'
        return [r for r in f]

    #for r in read1():
    #    pass

    for r in read0():
        pass
    time.sleep(10)
