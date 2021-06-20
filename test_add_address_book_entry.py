# -*- coding: utf-8 -*-
import unittest
import datetime
import pytest
from application import Application
from secondary import Secondary
from entry import Entry


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_address_book_entry(app):
    app.login("admin", "secret")
    app.fill_in_new_entry(Entry(firstname="Irina", middlename="MiddleName", lastname="LastName",
                                     nickname="insideout-oss", photo="/Users/Shared/python_training/photo.jpg", title="Mrs.",
                                     company="companyX", address="addressX",
                                     t_home="888888888", t_mobile="87777777777", t_work="567890987",
                                     t_fax="567890987",
                                     email="test email", email2="", email3="", homepage="https://homepage.it",
                                     birthdate=datetime.date(1999, 10, 8), anniversary=datetime.date(2000, 12, 29),
                                     secondary=Secondary("second address", "home phone", "notes")))
    app.logout()


def test_add_empty_address_book_entry(app):
    app.login("admin", "secret")
    app.fill_in_new_entry(Entry(firstname="", middlename="", lastname="",
                                     nickname="", photo=None, title="",
                                     company="", address="",
                                     t_home="", t_mobile="", t_work="",
                                     t_fax="",
                                     email="", email2="", email3="", homepage="",
                                     birthdate=None, anniversary=None,
                                     secondary=Secondary("", "", "")))
    app.logout()

