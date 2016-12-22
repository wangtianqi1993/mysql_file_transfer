#!/usr/bin/python
# -*- coding: utf-8 -*-

__author__ = 'wtq'

# ftp登录到的路径
FTP_PATH = "/home/wtq/"

# 要连接的远程主机ip
HOST = '10.108.112.74'
# 远程文件的路径，相对于ftp的登录路径而言,mysql应该备份到该路径下
TARGET_DIRN = 'ftp_file/'
# 要下载的目标文件名
TARGET_FILE = 'key_words.sql'
# 登录的ftp用户名
USER = "wtq"
# 登录的密码
PASSWD = "123"

# 要下载到的本地文件地址
DOWNLOAD_FILE = "/home/wtq/ftp_file/key_words.sql"

# 远程机上的mysql的配置
MYSQL_REMOTE_USER = "root"
MYSQL_REMOTE_PASSWORD = "123"
MYSQL_REMOTE_DATABASE = "yuqing"
MYSQL_REMOTE_TABLE = "t_items"

# 本地的mysql配置
MYSQL_LOCAL_USER = "root"
MYSQL_LOCAL_PASSWORD = "123"
MYSQL_LOCAL_DATABASE = "yuqing"
MYSQL_LOCAL_TABLE = "t_items"
