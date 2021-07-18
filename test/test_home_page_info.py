import re
from random import randrange


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

