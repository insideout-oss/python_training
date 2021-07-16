import re


def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[0]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.t_home == contact_from_edit_page.t_home
    assert contact_from_view_page.t_work == contact_from_edit_page.t_work
    assert contact_from_view_page.t_mobile == contact_from_edit_page.t_mobile
    assert contact_from_view_page.secondary.home == contact_from_edit_page.secondary.home


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_home_page(contact):
    secondary = contact.secondary.home if contact.secondary is not None else None
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.t_home,
                                        contact.t_mobile,
                                        contact.t_work,
                                        secondary]))))

