import random
import pytest
from pytest_bdd import given, when, then
from model.group import Group


@pytest.fixture
@given('a group list')
def group_list(db):
    return db.get_group_list()


@pytest.fixture
@given('a group with <name>, <header> and <footer>')
def new_group(name, header, footer):
    return Group(name, header, footer)


@when("I add the group to the list")
def add_new_group(app, new_group):
    app.group.create(new_group)


@then("the new group list is equal to the old list with the added new group")
def verify_group_added(db, group_list, new_group):
    old_groups = group_list
    old_groups.append(new_group)
    _new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(_new_groups, key=Group.id_or_max)


@pytest.fixture
@given('a non-empty group list')
def non_empty_group_list(db, app):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="some name"))
    return db.get_group_list()


@pytest.fixture
@given('a random group from the list')
def random_group(non_empty_group_list):
    return random.choice(non_empty_group_list)


@when('I delete the group from the list')
def delete_group(app, random_group):
    app.group.delete_group_by_id(random_group.id)


@then('the new group list is equal to the old group list without the deleted group')
def verify_group_deleted(db, non_empty_group_list, random_group, app, check_ui):
    old_groups = non_empty_group_list
    new_groups = db.get_group_list()
    assert len(old_groups) -1 == len(new_groups)
    old_groups.remove(random_group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


@when("I modify the group from the list")
def modify_random_group(app, random_group, new_group):
    new_group.id = random_group.id
    app.group.modify_group_by_id(new_group, random_group.id)


@then("the new group list is equal to the old group list with the modified group")
def verify_group_modified(db, check_ui, app, non_empty_group_list, new_group, random_group):
    old_groups = non_empty_group_list
    old_groups.remove(random_group)
    old_groups.append(new_group)
    new_groups = db.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
