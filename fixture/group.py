

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, group):
        self.open_groups_page()
        self.submit_new()
        self.fill_group_form(group)
        self.submit_submit()
        self.return_to_groups_page()

    def modify_first_group(self, group):
        self.open_groups_page()
        self.select_element()
        self.submit_edit()
        self.fill_group_form(group)
        self.submit_update()
        self.return_to_groups_page()

    def delete_first_group(self):
        self.open_groups_page()
        self.select_element()
        self.submit_delete()
        self.return_to_groups_page()

    def submit_new(self):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

    def submit_submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def submit_update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def submit_edit(self):
        wd = self.app.wd
        wd.find_element_by_name("edit").click()

    def select_element(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def submit_delete(self):
        wd = self.app.wd
        wd.find_element_by_name("delete").click()
