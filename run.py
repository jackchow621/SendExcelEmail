# -*- coding:utf-8 -*-
import os

from db import get_datas, get_fields
from email_util import create_email, send_email
from excel import get_excel
from date_utils import getYesterday


def main():
    # sender info
    sender = '*******************'
    password = '*******************'

    # receiver's list
    receiver = ['*******************', '*******************']

    sql = 'select * from table limit 10'
    # create data
    my_data = get_datas(sql)
    # create field
    my_field = get_fields(sql)
    # get yesterday's date str
    yesterdaystr = getYesterday()
    # file name
    my_file_name = 'data_' + yesterdaystr + '.xlsx'
    # file path
    file_path = 'D:/work/report/'
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    # create excel
    get_excel(my_data, my_field, file_path + my_file_name)

    email_to = ','.join(receiver)
    # email subject
    email_subject = 'data_' + yesterdaystr
    # email content
    email_content = 'Dear all,\n\tthe attachment is yesterday\'s data,please find..\n\njackchow '
    # attachment path
    attach_path = file_path + my_file_name
    # attachment name
    attach_name = my_file_name

    # create email
    msg = create_email(sender, email_to, email_subject,
                       email_content, attach_path, attach_name)
    # send email
    send_email(sender, password, receiver, msg)


if __name__ == "__main__":
    main();
