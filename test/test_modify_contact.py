import datetime
import os
from model.secondary import Secondary
from model.contact import Contact


def test_modify_contact(app):
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact(firstname="Modify", middlename="MiddleNameModify", lastname="Edited",
                               nickname="Edited-oss", photo=None, title=None,
                               company="Edited", address="Edited",
                               t_home="888888888", t_mobile="87777777777", t_work="567890987",
                               t_fax="567890987",
                               email="Edited", email2="", email3="", homepage="https://Edited.it",
                               birthdate=datetime.date(1999, 10, 8), anniversary=None,
                               secondary=Secondary("sEdited econd address", "Edited home phone", "Edited notes")))
    app.session.logout()


def test_modify_contact_birthdate(app):
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact(firstname=None, middlename=None, lastname=None,
                               nickname=None, photo=None, title=None,
                               company=None, address=None,
                               t_home=None, t_mobile=None, t_work=None, t_fax=None,
                               email=None, email2=None, email3=None, homepage=None,
                               birthdate=datetime.date(1999, 10, 8), anniversary=None,
                               secondary=None))
    app.session.logout()


def test_modify_contact_lastname(app):
    app.session.login("admin", "secret")
    app.contact.modify_first_contact(Contact(firstname=None, middlename=None, lastname="ModifiedLastName",
                               nickname=None, photo=None, title=None,
                               company=None, address=None,
                               t_home=None, t_mobile=None, t_work=None, t_fax=None,
                               email=None, email2=None, email3=None, homepage=None,
                               birthdate=None, anniversary=None,
                               secondary=None))
    app.session.logout()
