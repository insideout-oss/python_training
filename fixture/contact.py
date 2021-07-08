from selenium.webdriver.support.select import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_page(self):
        wd = self.app.wd
        if not(wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit"))):
            wd.find_element_by_link_text("add new").click()

    def select_first_contact(self):
        return self.select_contact_by_index(0)

    def get_contact_id_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()
        return wd.find_elements_by_name("selected[]")[index].get_attribute("value")

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def open_edit_page(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % str(id)).click()

    def accept_alert(self):
        wd = self.app.wd
        wd.switch_to_alert().accept()

    def submit_delete(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def submit_update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def submit_submit(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def return_to_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_value_without_click(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_select_value(self, field_name, value):
        wd = self.app.wd
        wd.find_element_by_name(field_name).click()
        Select(wd.find_element_by_name(field_name)).select_by_visible_text(value)

    def fill_contact(self, entry):
        wd = self.app.wd
        # fill in first name
        self.change_field_value("firstname", entry.firstname)
        self.change_field_value("middlename", entry.middlename)
        self.change_field_value("lastname", entry.lastname)
        self.change_field_value("nickname", entry.nickname)
        self.change_field_value_without_click("photo", entry.photo)
        self.change_field_value("title", entry.title)
        self.change_field_value("company", entry.company)
        self.change_field_value("address", entry.address)
        self.change_field_value("home", entry.t_home)
        self.change_field_value("mobile", entry.t_mobile)
        self.change_field_value("work", entry.t_work)
        self.change_field_value("fax", entry.t_fax)
        self.change_field_value("email", entry.email)
        self.change_field_value("email2", entry.email2)
        self.change_field_value("email3", entry.email3)
        self.change_field_value("homepage", entry.homepage)
        # Select b-day
        if entry.birthdate is not None:
            self.change_select_value("bday", str(entry.birthdate.day))
            self.change_select_value("bmonth", entry.birthdate.strftime("%B"))
            self.change_field_value("byear", str(entry.birthdate.year))
        # Select anniversary date
        if entry.anniversary is not None:
            self.change_select_value("aday", str(entry.anniversary.day))
            self.change_select_value("amonth", entry.anniversary.strftime("%B"))
            self.change_field_value("ayear", str(entry.anniversary.year))
        # Enter second address
        if entry.secondary is not None:
            self.change_field_value("address2", entry.secondary.address)
            self.change_field_value("phone2", entry.secondary.home)
            self.change_field_value("notes", entry.secondary.notes)

    def create(self, entry):
        self.open_add_new_page()
        self.fill_contact(entry)
        self.submit_submit()
        self.open_add_new_page()
        self.contact_cache = None

    def modify_first_contact(self, entry):
        self.modify_contact_by_index(entry, 0)

    def modify_contact_by_index(self, entry, index):
        self.app.open_home_page()
        self.select_contact_by_index(index)
        self.open_edit_page(self.get_contact_id_by_index(index))
        self.fill_contact(entry)
        self.submit_update()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        self.app.open_home_page()
        self.select_contact_by_index(index)
        self.submit_delete()
        self.accept_alert()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_first_contact_via_edit(self):
        self.delete_contact_via_edit_by_index(0)

    def delete_contact_via_edit_by_index(self, index):
        self.app.open_home_page()
        self.select_contact_by_index(index)
        self.open_edit_page(self.get_contact_id_by_index(index))
        self.submit_delete()
        self.app.open_home_page()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lname = element.find_element_by_xpath("//input[@id=%s]/following::td[1]" % str(id)).text
                fname = element.find_element_by_xpath("//input[@id=%s]/following::td[2]" % str(id)).text
                self.contact_cache.append(Contact(firstname=fname, lastname=lname, id=id))
        return list(self.contact_cache)
