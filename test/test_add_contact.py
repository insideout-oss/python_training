# -*- coding: utf-8 -*-
import datetime
import os
from model.secondary import Secondary
from model.contact import Contact


def test_add_address_book_entry(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact(firstname="Irina", middlename="MiddleName", lastname="LastName",
                               nickname="insideout-oss", photo=str(os.getcwd() + "/assets/photo.jpg"), title="Mrs.",
                               company="companyX", address="addressX",
                               t_home="888888888", t_mobile="87777777777", t_work="567890987",
                               t_fax="567890987",
                               email="test email", email2="", email3="", homepage="https://homepage.it",
                               birthdate=datetime.date(1999, 10, 8), anniversary=datetime.date(2000, 12, 29),
                               secondary=Secondary("second address", "home phone", "notes")))
    app.session.logout()


def test_add_empty_address_book_entry(app):
    app.session.login("admin", "secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="",
                               nickname="", photo=None, title="",
                               company="", address="",
                               t_home="", t_mobile="", t_work="",
                               t_fax="",
                               email="", email2="", email3="", homepage="",
                               birthdate=None, anniversary=None,
                               secondary=Secondary("", "", "")))
    app.session.logout()

