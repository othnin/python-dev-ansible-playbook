#!/usr/bin/python

if __name__ == "__main__":
    print "Start"
    f = open('/tmp/test_python','w')
    f.write('Hi there\n')
    f.close()
    print "End"