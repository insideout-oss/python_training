import re
from random import randrange
from model.contact import Contact


def test_home_page_info_compare_with_edit_page(app):
    index = randrange(app.contact.count())
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_emails_from_home_page == app.contact.merge_data_like_on_home_page(
        [contact_from_edit_page.email,
         contact_from_edit_page.email2,
         contact_from_edit_page.email3],
        app.contact.remain)
    assert contact_from_home_page.all_phones_from_home_page == app.contact.merge_data_like_on_home_page(
        [contact_from_edit_page.t_home,
         contact_from_edit_page.t_mobile,
         contact_from_edit_page.t_work,
         contact_from_edit_page.secondary.home if contact_from_edit_page.secondary is not None else None],
        app.contact.clear)
    assert contact_from_home_page.homepage == contact_from_edit_page.homepage


def test_home_page_info_compare_with_database(app, db):
    c_from_hp = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    c_from_db = sorted(db.get_contact_list(), key=Contact.id_or_max)
    assert len(c_from_hp) == len(c_from_db)
    for i in range(0, len(c_from_db)):
        assert c_from_hp[i].lastname == c_from_db[i].lastname
        assert c_from_hp[i].firstname == c_from_db[i].firstname
        assert c_from_hp[i].address == app.contact.merge_data_like_on_home_page([c_from_db[i].address],
                                                                                app.contact.clear_specsym)
        assert c_from_hp[i].all_emails_from_home_page == app.contact.merge_data_like_on_home_page(
            [c_from_db[i].email,
             c_from_db[i].email2,
             c_from_db[i].email3],
            app.contact.remain)
        assert re.sub("\n+", "\n", c_from_hp[i].all_phones_from_home_page) == app.contact.merge_data_like_on_home_page(
            [c_from_db[i].t_home,
             c_from_db[i].t_mobile,
             c_from_db[i].t_work,
             c_from_db[i].secondary.home if c_from_db[i].secondary is not None else None],
            app.contact.clear)
        assert c_from_hp[i].homepage == c_from_db[i].homepage


