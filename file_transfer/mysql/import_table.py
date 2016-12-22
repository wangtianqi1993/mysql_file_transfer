#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wtq'

import subprocess
from config.config import MYSQL_LOCAL_USER, MYSQL_LOCAL_PASSWORD
from config.config import MYSQL_LOCAL_DATABASE, MYSQL_LOCAL_TABLE
from config.config import DOWNLOAD_FILE


def import_table():
    """
    import mysql表到数据库
    :return:
    """
    try:
        mysqlimport_command = "mysql -u" + MYSQL_LOCAL_USER + " -p" + MYSQL_LOCAL_PASSWORD + " " + MYSQL_LOCAL_DATABASE +\
                              " < " + DOWNLOAD_FILE
        print mysqlimport_command
        ps = subprocess.Popen(mysqlimport_command, shell=True)
        ps.wait()
        print 'mysql import over '
    except Exception, e:
        print "import error", e

if __name__ == "__main__":
    import_table()
