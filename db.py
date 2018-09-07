# -*- coding:utf-8 -*-
import json
import sys

import pymysql as pms

from config import *
from db_pool import Mysql

reload(sys)
sys.setdefaultencoding('utf-8')


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


def get_datas_pool(sql):
    # create the database connection
    conn = Mysql()
    # get data
    datas = conn.getAll(sql)
    result = []
    if datas:
        for row in datas:
            # for i in range(len(row)):
            #     if isinstance(row[i], long):
            #         time_local = time.localtime(row[i])
            #         row[i] = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
            #     print row[i]
            json_str = json.dumps(row, ensure_ascii=False)
            result.append(json.loads(json_str, encoding='utf-8'))
            # dict to tuple
            # result.append(tuple(str.values()))
    else:
        result = False
    return result


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


def get_fields_pool(sql):
    conn = Mysql()
    # get fields
    fields = conn.getFields(sql)
    # print fields
    return fields


if __name__ == '__main__':
    # data = get_datas('select * from lzh_activities limit 10')
    # print json.dumps(data, encoding='UTF-8', ensure_ascii=False)

    data = get_datas_pool('select * from lzh_activities limit 10')
    # print data

    # data = get_fields('select * from lzh_activities limit 10')
    # print data

    # data = get_fields_pool('select * from lzh_activities limit 10')
    # print data
