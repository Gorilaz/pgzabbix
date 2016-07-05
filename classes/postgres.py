#!/usr/bin/python

__author__="Paulo Victor Maluf"
__date__ ="$27/10/2014 13:35:12$"

from connection import Connect;

class Postgres(object):
    
    def __init__(self, dsn=None):
        self.dsn = dsn
        self.connect()

    def connect(self):
        conn = Connect(self.dsn)
        self.cursor = conn.cur()

    def exec_sql(self, sql): 
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def __del__(self):
        del self
