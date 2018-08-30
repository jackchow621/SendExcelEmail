# -*- coding:utf-8 -*-
import pymysql as pms

from config import *


def get_datas(sql):
    # create the database connection
    conn = pms.connect(host=DB_URL, user=DB_USER, passwd=DB_PASSWORD,
                       database=DB_DATABASE, port=DB_PORT,
                       charset=DB_CHARSET)
    # create cursor
    cur = conn.cursor()
    # execute sql
    cur.execute(sql)
    # get data
    datas = cur.fetchall()
    print(datas)
    # close the connection
    cur.close()
    return datas


def get_fields(sql):
    conn = pms.connect(host=DB_URL, user=DB_USER, passwd=DB_PASSWORD,
                       database=DB_DATABASE, port=DB_PORT,
                       charset=DB_CHARSET)
    cur = conn.cursor()
    cur.execute(sql)
    # get fields
    fields = cur.description
    cur.close()
    return fields


if __name__ == '__main__':
    get_datas()
