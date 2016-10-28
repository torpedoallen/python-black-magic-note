# coding=utf8

import contextlib

global connects
connects = 0

class Database(object):

    def __init__(self):
        self.connected = False

    def connect(self):
        global connects 
        connects += 1

        self.connected = True

    def close(self):
        global connects 
        connects -= 1
        self.connected = False

    def query(self):
        if self.connected:
            return 'query data'
        else:
            raise ValueError('DB not connected ')

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            print 'exit'
        except:
            import traceback
            traceback.print_exc()
        finally:
            self.close()



def handle_query0():
    global connects
    print 'before TIME_WAIT', connects
    db = Database()
    for i in range(5):
        db.connect()
        print 'handle --- %s' % (i+1), db.query()
        #db.close()

    print 'after TIME_WAIT', connects

def handle_query1():
    global connects
    print 'before TIME_WAIT', connects
    with Database() as db:
        for i in range(5):
            print 'handle --- %s' % (i+1), db.query()

    print 'after TIME_WAIT', connects



def main():
    handle_query0()
    handle_query1()

if __name__ == '__main__':
    main()
