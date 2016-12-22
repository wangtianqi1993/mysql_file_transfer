#!/usr/bin/python  
# -*- coding: utf-8 -*-

__author__ = 'wtq'

import ftplib
import os
import socket

from config.config import HOST
from config.config import TARGET_DIRN
from config.config import TARGET_FILE, DOWNLOAD_FILE
from config.config import USER
from config.config import PASSWD


def file_transfer():
    """

    :return:
    """
    try:
        f = ftplib.FTP(HOST)
    except (socket.error, socket.gaierror):
        print 'ERROR:cannot reach " %s"' % HOST
        return
    print '***Connected to host "%s"' % HOST

    try:
        f.login(USER, PASSWD)
    except ftplib.error_perm:
        print 'ERROR: cannot login anonymously'
        f.quit()
        return
    print '*** Logged success"'

    try:
        f.cwd(TARGET_DIRN)
    except ftplib.error_perm:
        print 'ERRORL cannot CD to "%s"' % TARGET_DIRN
        f.quit()
        return

    print '*** Changed to "%s" folder' % TARGET_DIRN

    try:
        # 传一个回调函数给retrbinary() 它在每接收一个二进制数据时都会被调用

        # file write 是要操作的本地文件对象
        file_write = open(DOWNLOAD_FILE, 'wb')

        # file name 是要下载的远程文件的名字
        file_name = 'RETR ' + TARGET_FILE
        f.retrbinary(file_name, file_write.write)

    except ftplib.error_perm:
        print 'ERROR: cannot read file "%s"' % TARGET_FILE
        os.unlink(TARGET_FILE)
    else:
        print '*** Downloaded "%s" to CWD' % TARGET_FILE
    f.quit()

    return


if __name__ == '__main__':
    file_transfer()
