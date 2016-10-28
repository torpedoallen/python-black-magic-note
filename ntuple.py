# coding=utf8



import time
from collections import namedtuple



Event = namedtuple("Event", ['date', 'name', 'participants'])
evs = [Event('2016.1.%s' % (i+1), 'event %s' % i, '%s' % i) for i in xrange(100000)]
print evs[0].date
print evs[0].name
print evs[0].participants


#class Event2(object):
#
#    def __init__(self, date_, name, participants):
#        self.date_ = date_
#        self.name = name
#        self.participants = participants
#
#evs = [Event2('2016.1.%s' % (i+1), 'event %s' % i, '%s' % i) for i in xrange(100000)]

time.sleep(10)

