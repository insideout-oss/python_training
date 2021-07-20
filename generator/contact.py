# -*- coding: utf-8 -*-
import datetime
import getopt
import os.path
import random
import string
import jsonpickle
import sys

from model.secondary import Secondary
from model.contact import Contact


try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)


n = 5
f = "data/contacts.json"


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_phone(maxlen):
    symbols = string.digits + "()-"
    return "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_date():
    start_date = datetime.date(1980, 1, 1)
    end_date = datetime.date(2020, 2, 1)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    return start_date + datetime.timedelta(days=random_number_of_days)


testdata = [Contact(firstname="", middlename="", lastname="",
                nickname="", photo=None, title="",
                company="", address="",
                t_home="", t_mobile="", t_work="",
                t_fax="",
                email="", email2="", email3="", homepage="",
                birthdate=None, anniversary=None,
                secondary=Secondary("", "", ""))] + [
        Contact(firstname=random_string("firstname", 10),
                middlename=random_string("middlename", 10),
                lastname=random_string("lastname", 10),
                nickname=random_string("nickname", 10),
                photo=None, title=random_string("title", 10),
                company=random_string("company", 10),
                address=random_string("address", 10),
                t_home=random_phone(8), t_mobile=random_phone(8), t_work=random_phone(8), t_fax=random_phone(8),
                email=random_string("email", 5) + "@test.com",
                email2=random_string("email2", 5) + "@test.com",
                email3=random_string("email3", 5) + "@test.com",
                homepage=random_string("https://", 10),
                birthdate=random_date(), anniversary=random_date(),
                secondary=Secondary(random_string("address", 10), random_phone(8), random_string("notes", 10)))
        for i in range(5)]


file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))

