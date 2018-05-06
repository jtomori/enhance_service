import time

def slow_job(arg):
    for i in xrange(10):
        print str(i) + ": " + arg
        time.sleep(2)