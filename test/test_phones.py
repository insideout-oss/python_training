import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    all_phones = app.contact.merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_phones_from_home_page == all_phones



