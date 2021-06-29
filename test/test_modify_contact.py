import datetime
import os
from model.secondary import Secondary
from model.contact import Contact


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="NameBefore Modify"))
    app.contact.modify_first_contact(Contact(firstname="Modify", middlename="MiddleNameModify", lastname="Edited",
                               nickname="Edited-oss", photo=None, title=None,
                               company="Edited", address="Edited",
                               t_home="888888888", t_mobile="87777777777", t_work="567890987",
                               t_fax="567890987",
                               email="Edited", email2="", email3="", homepage="https://Edited.it",
                               birthdate=datetime.date(1999, 10, 8), anniversary=None,
                               secondary=Secondary("Edited second address", "Edited home phone", "Edited notes")))


def test_modify_contact_birthdate(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(birthdate=datetime.date(1981, 1, 8)))
    app.contact.modify_first_contact(Contact(birthdate=datetime.date(1995, 2, 1)))


def test_modify_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="lastname"))
    app.contact.modify_first_contact(Contact(lastname="ModifiedLastName"))


def test_modify_contact_address(app):
    if app.contact.count() == 0:
        app.contact.create(Contact())
    app.contact.modify_first_contact(Contact(address="AddressModified"))