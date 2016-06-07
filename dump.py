#!/usr/bin/env python
import ConfigParser
import os
import time
import getpass
import boto3

def get_dump():

    database = "DATABASE_NAME"
    user ="ROOT"
    password = "ADMIN"
    host = "HOST_NAME"
    filestamp = time.strftime('%d_%b_%Y_%H_%M')
    os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s | gzip -c > %s.gz" % (user,password,host,database,database+"_"+filestamp))
    my_file=open(database+"_"+filestamp+".gz")
    s3 = boto3.resource('s3')
    s3.Bucket('sqy').put_object(Key='connect/db_backups/' + database+"_"+filestamp+".gz", Body=my_file,
                                        ContentDisposition="inline; filename=" + database+"_"+filestamp+".gz")


if __name__=="__main__":
    get_dump()
