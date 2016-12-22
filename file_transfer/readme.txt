本项目功能实现mysql数据库的备份,然后将备份后的sql文件从远程通过ftp拷贝到本地，将本地的sql文件导入到本地的mysql中。
使用时本项目应该在远程机上与本地各自放置一份，在config中分别更改ftp用户名密码,数据库的配置,文件的路径等。

执行的步骤如下：
（1） 在远程机器上执行mysql中的dump_table.py 备份目标数据库生成sql文件
（2） 执行ftp中的ftp_transfer_file.py 来实现将远程的sql文件传输到本地
（3） 在本地执行mysql中的import_table.py 来实现sql文件导入到本地的mysql中
