#!/usr/bin/python
#
# pgzabbix - PostgreSQL for Zabbix monitoring
# Criacao: Paulo Victor Maluf Alves - 10/2014
#
# Changelog:
#
# Date       Author              Description
# ---------- ------------------- ----------------------------------------------------
# ====================================================================================

__author__="Paulo Victor Maluf"
__date__ ="$27/10/2014 13:00:03$"

import os
import pprint
import optparse
import subprocess
from optparse import OptionParser

from classes import Postgres
from classes import Logger

# Global variables
script_dir = os.path.dirname(__file__)
hostname = os.uname()[1]
application = 'PostgreSQL'
db_file = script_dir + '/pgzbx.db'
config_file = script_dir + '/conf/pgzabbix.conf'
zbx_sender = '/usr/bin/zabbix_sender'
zbx_config = '/etc/zabbix/zabbix_agentd.conf'

def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option('-H', '--host', action='store', type='string', dest='host', default='127.0.0.1', help='The hostname you want to connect to')
    parser.add_option('-P', '--port', action='store', type='int',    dest='port', default=5432,        help='The port postgresql is runnung on')
    parser.add_option('-u', '--user', action='store', type='string', dest='user', default='postgres',  help='The username you want to login as')
    parser.add_option('-p', '--pass', action='store', type='string', dest='passwd', default='',        help='The password you want to use for that user')
    parser.add_option('-s', '--slow-query-threshold', action='store', type='string', dest='slowquery', default='180', help='Threshold in seconds for slow query')
    parser.add_option('-d', '--database', action='store', type='string', dest='db', default='postgres', help='The password you want to use for that user')
    (options, args) = parser.parse_args()
    
    dsn = "host='%s' port='%s' dbname='%s' user='%s' password='%s'" % (options.host, options.port, options.db, options.user, options.passwd)
 
    pg = Postgres(dsn=dsn)
    log = Logger()

    # truncate db file 
    log.trunc(db_file)

    try:
        with open(config_file, 'rt') as file:
            for line in file:
                if not line.strip().startswith('#'):
                    line = line.replace('<SLOWQUERY>', options.slowquery).replace('<DB>', options.db).split('|')
                    value = pg.exec_sql(line[1])
                    fvalue = ''.join([s[0].__str__() + ' ' for s in value])
                    item = line[0]
                    zbx =  "%s %s[%s] %s\n" % ( hostname, application, item, fvalue) 
                    log.write(db_file, zbx)
    except IOError, e:
        return e 

    if os.path.isfile(zbx_sender):
        subprocess.call([zbx_sender, "-c", zbx_config, "-i", db_file])
    else:
        print "Sorry, %s not found." % zbx_sender
    

if __name__ == "__main__":
    main()
