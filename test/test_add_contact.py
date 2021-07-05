# -*- coding: utf-8 -*-
import datetime
import os
from model.secondary import Secondary
from model.contact import Contact


def test_add_none_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Name2", middlename="MiddleName2", lastname="LastName2",
                               nickname="insideout-oss", photo=str(os.getcwd() + "/assets/photo.jpg"), title="Mrs.",
                               company="companyX", address="addressX",
                               t_home="888888888", t_mobile="87777777777", t_work="567890987",
                               t_fax="567890987",
                              email="test email", email2=None, email3=None, homepage="https://homepage.it",
                               birthdate=datetime.date(1900, 1, 1), anniversary=datetime.date(1950, 3, 3),
                               secondary=Secondary("second address", "home phone", "notes"))
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


#def test_add_empty_contact(app):
#    app.contact.create(Contact(firstname="", middlename="", lastname="",
#                               nickname="", photo=None, title="",
#                               company="", address="",
#                               t_home="", t_mobile="", t_work="",
#                               t_fax="",
#                               email="", email2="", email3="", homepage="",
#                               birthdate=None, anniversary=None,
#                               secondary=Secondary("", "", "")))

