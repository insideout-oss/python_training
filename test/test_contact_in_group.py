from model.group import Group
from model.contact import Contact
import random
from random import randrange


def test_add_some_contact_to_some_group(app, ormdb):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First name", middlename="MiddleName", lastname="LastName"))
    if app.group.count() == 0:
        app.group.create(Group(name="name_edited", header="header_edited", footer="footer_edited"))
    # Get contacts that are not in groups
    contacts = ormdb.get_contacts_without_group()
    if len(contacts) == 0:
        # Search for contacts that are at least not in one group
        contacts = ormdb.get_contacts_without_at_least_one_group()
        if len(contacts) == 0:
            app.contact.create(Contact(firstname="First name with empty group", middlename="MiddleName", lastname="LastName"))
            contacts = ormdb.get_contacts_without_group()
            assert len(contacts) == 1
    # Perform adding test
    c_index = randrange(len(contacts))
    groups = ormdb.get_groups_without_contact(contacts[c_index])
    g_index = randrange(len(groups))
    contacts_in_group_before = ormdb.get_contacts_in_group(groups[g_index])
    app.contact.add_contact_to_group(contacts[c_index], groups[g_index])
    contacts_in_group_after = ormdb.get_contacts_in_group(groups[g_index])
    contacts_in_group_before.append(contacts[c_index])
    assert sorted(contacts_in_group_before, key=Contact.id_or_max) == sorted(contacts_in_group_after, key=Contact.id_or_max)


def test_delete_contact_from_some_group(app, ormdb):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="First name", middlename="MiddleName", lastname="LastName"))
    if app.group.count() == 0:
        app.group.create(Group(name="name_edited", header="header_edited", footer="footer_edited"))
    # Get current values and generate indexes randomly
    all_groups_with_contacts = ormdb.get_groups_with_contacts()
    # In case no contacts in any group - add random contact to random group
    if len(all_groups_with_contacts) == 0:
        contacts = ormdb.get_contact_list()
        c_index = randrange(len(contacts))
        groups = ormdb.get_group_list()
        g_index = randrange(len(groups))
        app.contact.add_contact_to_group(contacts[c_index], groups[g_index])
        all_groups_with_contacts = ormdb.get_groups_with_contacts()
        assert len(all_groups_with_contacts) == 1
    # Continue test with deleting contact from group
    g_index = randrange(len(all_groups_with_contacts))
    group = all_groups_with_contacts[g_index]
    contacts_in_group_before = ormdb.get_contacts_in_group(group)
    c_index = randrange(len(contacts_in_group_before))
    contact = contacts_in_group_before[c_index]
    # Remove contact from group via UI
    app.contact.remove_contact_from_group(contact, group)
    # Get changes values
    contacts_in_group_after = ormdb.get_contacts_in_group(group)
    contacts_in_group_before.remove(contact)
    assert sorted(contacts_in_group_before, key=Contact.id_or_max) == sorted(contacts_in_group_after,
                                                                             key=Contact.id_or_max)
