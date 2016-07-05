#!/usr/bin/python

__author__="Paulo Victor Maluf"
__date__ ="$27/10/2014 13:33:27$"

import sys

try:
    import psycopg2
except ImportError, e:
    print e
    sys.exit(-1)

class Connect:

    global cur;

    def __init__(self, dsn):
        try:
            conn_string = "%s" % dsn
            #print "Connecting to database\n ->%s" % (conn_string)
            conn = psycopg2.connect(conn_string)
            self.cur = conn.cursor;
        except Exception, e:
            print e
            sys.exit(-1)
       
    def __del__(self):
        #print "Connection closed!";
        del self;
