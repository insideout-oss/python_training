from model.group import Group


def test_modify_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="", header="", footer=""))
    old_groups = app.group.get_group_list()
    group = Group(name="name_edited", header="header_edited", footer="footer_edited")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_first_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Needs to be modified"))
    old_groups = app.group.get_group_list()
    group = Group(name="name_edited")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(header="Needs to be modified"))
    old_groups = app.group.get_group_list()
    group = Group(header="Header modified")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



def test_modify_first_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(footer="Needs to be modified"))
    old_groups = app.group.get_group_list()
    group = Group(footer="Header modified")
    group.id = old_groups[0].id
    app.group.modify_first_group(group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
