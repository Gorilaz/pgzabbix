# pgzabbix

My first Python script to monitoring PostgreSQL on Zabbix using zabbix_sender

## Notice

This script was tested in:

* Linux
  * OS Distribution: CentOS release 6.5 (Final)
  * Python: 2.6.6

## Prerequisities

* psycopg2

## How to use it

```
/u00/scripts/postgres/pgzabbix/pgzabbix.py --help
Usage: pgzabbix.py [options] arg

Options:
  -h,           --help        show this help message and exit
  -H HOST,      --host=HOST   The hostname you want to connect to
  -P PORT,      --port=PORT   The port postgresql is runnung on
  -u USER,      --user=USER   The username you want to login as
  -p PASSWD,    --pass=PASSWD The password you use for that user
  -s SLOWQUERY, --slow-query-threshold=SLOWQUERY
                              Threshold in seconds for slow query
  -d DB,        --database=DB The database you want to monitoring
```

* Ensure that zabbix_agentd is up and running, and schedule the pgzabbix.py on crontab or cron.d. 

Example:
```
# Postgres Graph
*/5 * * * * /u00/scripts/postgres/pgzabbix/pgzabbix.py -d mydatabase > /dev/null 2>&1 
```

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
