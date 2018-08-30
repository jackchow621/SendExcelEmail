# -*- coding:utf-8 -*-
import datetime


def getYesterday():
    today = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    yesterday = today - oneday
    yesterdaystr = yesterday.strftime('%Y%m%d')
    return yesterdaystr
