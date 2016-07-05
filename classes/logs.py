#!/usr/bin/python

__author__="Paulo Victor Maluf"
__date__ ="$27/10/2014 13:35:12$"

import os

class Logger:

    def ensure_dir(self,f):
        d = os.path.dirname(f)
        if not os.path.exists(d):
            os.makedirs(d)

    def write(self, file_name, string):
        try:
            f = open(file_name, 'a')
            f.write(string)
            f.close()
        except Exception, e:
            print e

    def read(self, file_name):
        try:
            f = open(file_name, 'r')
            data = f.read()
            f.close()
        except Exception, e:
            print e

    def trunc(self, file_name): 
        try:
            f = open(file_name,'w')
            f.truncate()
            f.close()
        except Exception, e:
            print e
