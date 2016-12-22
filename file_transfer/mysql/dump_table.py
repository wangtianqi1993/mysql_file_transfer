#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'wtq'

import datetime
import subprocess
from config.config import FTP_PATH
from config.config import TARGET_DIRN
from config.config import TARGET_FILE
from config.config import MYSQL_REMOTE_USER, MYSQL_REMOTE_PASSWORD
from config.config import MYSQL_REMOTE_DATABASE, MYSQL_REMOTE_TABLE

download_sql_path = FTP_PATH + TARGET_DIRN + TARGET_FILE


def dump_table():
    """
    备份mysql的item表中今天爬到的数据到download_sql_path
    :return:
    """
    try:

        today = datetime.date.today()
        use_today = "'%s'" % str(today)
        filter = ' -w"DATE(crawl_time)>%s"' % use_today

        mysqldump_command = "mysqldump --no-create-info -u " + MYSQL_REMOTE_USER + " -p" + MYSQL_REMOTE_PASSWORD +\
                               filter + " " + MYSQL_REMOTE_DATABASE + " " + MYSQL_REMOTE_TABLE + " " + "> " + download_sql_path

        print mysqldump_command
        ps = subprocess.Popen(mysqldump_command, shell=True)
        ps.wait()

        print 'mysql dump over '
    except Exception, e:
        print "mysql dump error", e

if __name__ == "__main__":
    dump_table()
    # print datetime.date.today(), type(datetime.date.today())

