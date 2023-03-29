# Проанализируйте данные, полученные от ЦАП. Для этого можно воспользоваться приведенным ниже кодом.

import csv
import datetime
from matplotlib import pyplot as plt
import locale
import random
from random import *

def parse_time(text):
    return datetime.datetime.strptime(text, '%Y-%m-%d %H:%M:%S.%f')


def load_csv(filename):
    with open(filename, encoding='utf8') as f:
        return list(csv.reader(f, delimiter=','))


# id, task, variant, group, time
messages = load_csv('messages.csv')

if __name__ == "hw3":
    print(messages)

# id, message_id, time, status
checks = load_csv('checks.csv')

# task, variant, group, time, status, achievements
statuses = load_csv('statuses.csv')

# О статусах см. https://github.com/kispython-ru/dta/blob/main/webapp/models.py#L44-L50


# Обновляем локаль с английского на русский
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
