# -*- coding:utf-8 -*-
import os

from config import EXE_SQL, SEND_EMAIL, SEND_PWD, RECEIVE_EMAIL, FILE_NAME, FILE_SUFFIX, FILE_PATH, EMAIL_CONTENT
from db import get_fields, get_datas_pool, get_fields_pool
from email_util import create_email, send_email
from excel import get_excel
from date_utils import getYesterday


def main():
    # sender info
    sender = SEND_EMAIL
    password = SEND_PWD

    # receiver's list
    receiver = RECEIVE_EMAIL

    sql = EXE_SQL
    # create data
    # my_data = get_datas(sql)
    my_data = get_datas_pool(sql)
    # create field
    # my_field = get_fields(sql)
    my_field = get_fields_pool(sql)
    # get yesterday's date str
    yesterdaystr = getYesterday()
    # file name
    my_file_name = FILE_NAME + yesterdaystr + FILE_SUFFIX
    # file path
    file_path = FILE_PATH
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    # create excel
    get_excel(my_data, my_field, file_path + my_file_name)

    email_to = ','.join(receiver)
    # email subject
    email_subject = FILE_NAME + yesterdaystr
    # email content
    email_content = EMAIL_CONTENT
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
