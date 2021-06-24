

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        # delete
        wd.find_element_by_name("selected[]").click()
        # submit delete
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def get_group(self, index):
        wd = self.app.wd
        # Assume we are on group page already
        ids = wd.find_elements_by_name("selected[]")
        if index in range(0, len(ids)):
            return ids[index]
        return wd.find_element_by_name("selected[]")

    def delete(self, index):
        wd = self.app.wd
        self.open_groups_page()
        self.get_group(index).click()
        # submit delete
        wd.find_element_by_name("delete").click()
        self.return_to_groups_page()

    def modify(self, group, index):
        wd = self.app.wd
        self.open_groups_page()
        # Select group by index
        self.get_group(index).click()
        # Edit group
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def modify_name(self, name, index):
        wd = self.app.wd
        self.open_groups_page()
        # Select group by index
        self.get_group(index).click()
        # Edit group
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def modify_header(self, header, index):
        wd = self.app.wd
        self.open_groups_page()
        # Select group by index
        wd.find_element_by_xpath("//div[@id='content']/form/span["+str(index)+"]/input").click()
        # Edit group
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()

    def modify_footer(self, footer, index):
        wd = self.app.wd
        self.open_groups_page()
        # Select group by index
        wd.find_element_by_xpath("//div[@id='content']/form/span["+str(index)+"]/input").click()
        # Edit group
        wd.find_element_by_name("edit").click()
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        wd.find_element_by_name("update").click()
        self.return_to_groups_page()
