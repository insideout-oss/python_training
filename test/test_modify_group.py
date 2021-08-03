from random import randrange
import random
from model.group import Group


def test_modify_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="", header="", footer=""))
    old_groups = db.get_group_list()
    group_old = random.choice(old_groups)
    group_mdf = Group(name="name_edited", header="header_edited", footer="footer_edited", id=group_old.id)
    app.group.modify_group_by_id(group_mdf, group_old.id)
    new_groups = db.get_group_list()
    old_groups = list(map(lambda x: x if x != group_old else group_mdf, old_groups))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_some_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Needs to be modified"))
    old_groups = db.get_group_list()
    group_old = random.choice(old_groups)
    group = Group(name="name_edited")
    group.id = group_old.id
    app.group.modify_group_by_id(group, group_old.id)
    new_groups = db.get_group_list()
    old_groups = list(map(lambda x: x if x != group_old else group, old_groups))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_some_group_header(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(header="Needs to be modified"))
    old_groups = db.get_group_list()
    group_old = random.choice(old_groups)
    group = Group(header="Header modified")
    group.id = group_old.id
    app.group.modify_group_by_id(group, group_old.id)
    new_groups = db.get_group_list()
    old_groups = list(map(lambda x: x if x != group_old else group, old_groups))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_some_group_footer(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(footer="Needs to be modified"))
    old_groups = db.get_group_list()
    group_old = random.choice(old_groups)
    group_mdf = Group(footer="Header modified")
    group_mdf.id = group_old.id
    app.group.modify_group_by_id(group_mdf, group_old.id)
    new_groups = db.get_group_list()
    old_groups = list(map(lambda x: x if x != group_old else group_mdf, old_groups))
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
