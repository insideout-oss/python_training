import datetime
import os
from model.secondary import Secondary
from model.contact import Contact


def test_modify_contact_firstname(app):
    app.session.login("admin", "secret")
    app.contact.modify_field(element_name="firstname", element_value="EditByTestName",
                             index=10)
    app.session.logout()


def test_modify_contact_lastname(app):
    app.session.login("admin", "secret")
    app.contact.modify_field(element_name="lastname", element_value="EditedByTestLastName",
                             index=30)
    app.session.logout()


def test_modify_contact(app):
    app.session.login("admin", "secret")
    app.contact.modify(Contact(firstname="IrinaModify", middlename="MiddleNameModify", lastname="Edited",
                               nickname="Edited-oss", photo=None, title="Mrs.",
                               company="Edited", address="Edited",
                               t_home="888888888", t_mobile="87777777777", t_work="567890987",
                               t_fax="567890987",
                               email="Edited", email2="", email3="", homepage="https://Edited.it",
                               birthdate=datetime.date(1999, 10, 8), anniversary=datetime.date(2000, 12, 29),
                               secondary=Secondary("sEdited econd address", "Edited home phone", "Edited notes")),
                       index=1)
    app.session.logout()
