from selenium.webdriver.support.select import Select
from model.contact import Contact
from model.secondary import Secondary
import re


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

    def select_add_to_group(self, group):
        wd = self.app.wd
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_value(group.id)

    def select_contacts_in_group(self, group):
        wd = self.app.wd
        wd.find_element_by_name("group").click()
        Select(wd.find_element_by_name("group")).select_by_value(group.id)

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def open_edit_page(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@href='edit.php?id=%s']" % str(id)).click()

    def press_add_to_group(self):
        wd = self.app.wd
        wd.find_element_by_name("add").click()

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

    def submit_remove(self):
        wd = self.app.wd
        wd.find_element_by_name("remove").click()

    def return_to_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def get_field_value(self, field_name):
        wd = self.app.wd
        return wd.find_element_by_name(field_name).get_attribute("value")

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
        self.open_contact_edit_page_by_index(index)
        self.fill_contact(entry)
        self.submit_update()
        self.app.open_home_page()
        self.contact_cache = None

    def modify_contact_by_id(self, entry, id):
        self.open_contact_edit_page_by_id(id)
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

    def delete_contact_by_id(self, id):
        self.app.open_home_page()
        self.select_contact_by_id(id)
        self.submit_delete()
        self.accept_alert()
        self.app.open_home_page()
        self.contact_cache = None

    def delete_first_contact_via_edit(self):
        self.delete_contact_via_edit_by_index(0)

    def delete_contact_via_edit_by_index(self, index):
        self.open_contact_edit_page_by_index(index)
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
                cells = element.find_elements_by_tag_name("td")
                all_phones = cells[5].text
                all_emails = cells[4].text
                address = cells[3].text
                images = element.find_elements_by_tag_name("img")
                homepage = element.find_element_by_xpath("//input[@id=%s]/following::td[9]/a/img" % str(id)).\
                    get_attribute("title") if len(images) == 4 else ''
                self.contact_cache.append(Contact(firstname=fname, lastname=lname, id=id,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails,
                                                  address=address,
                                                  homepage=homepage))
        return list(self.contact_cache)

    def open_contact_edit_page_by_index(self, index):
        self.app.open_home_page()
        self.select_contact_by_index(index)
        self.open_edit_page(self.get_contact_id_by_index(index))

    def open_contact_edit_page_by_id(self, id):
        self.app.open_home_page()
        self.select_contact_by_id(id)
        self.open_edit_page(id)

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_edit_page_by_index(index)
        firstname = self.get_field_value("firstname")
        lastname = self.get_field_value("lastname")
        id = self.get_field_value("id")
        home = self.get_field_value("home")
        work = self.get_field_value("work")
        mobile = self.get_field_value("mobile")
        phone2 = self.get_field_value("phone2")
        email1 = self.get_field_value("email")
        email2 = self.get_field_value("email2")
        email3 = self.get_field_value("email3")
        homepage = self.get_field_value("homepage")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       t_home=home, t_work=work,
                       t_mobile=mobile, secondary=Secondary(home=phone2),
                       email=email1, email2=email2, email3=email3,
                       homepage=homepage)

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        id = self.get_contact_id_by_index(index)
        wd.find_element_by_xpath("//a[@href='view.php?id=%s']" % str(id)).click()

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        t_home = re.search("H: (.*)", text)
        t_work = re.search("W: (.*)", text)
        t_mobile = re.search("M: (.*)", text)
        secondary_home = re.search("P: (.*)", text)
        return Contact(t_home=t_home, t_work=t_work, t_mobile=t_mobile, secondary=Secondary(home=secondary_home))

    def clear(self, s):
        return re.sub("[() -]", "", s)

    def clear_specsym(self, s):
        tmp = re.sub(" +", " ", s)
        return re.sub("\r", "", tmp)

    def remain(self, s):
        return s

    def merge_data_like_on_home_page(self, entry_list, func):
        return "\n".join(filter(lambda x: x != "",
                                map(lambda x: func(x),
                                    filter(lambda x: x is not None, entry_list))))

    def merge_phones_like_on_home_page(self, contact):
        secondary = None
        if contact.secondary is not None:
            secondary = contact.secondary.home

        return self.merge_data_like_on_home_page([contact.t_home, contact.t_mobile, contact.t_work, secondary],
                                                 self.clear)

    def add_contact_to_group(self, contact, group):
        self.app.open_home_page()
        self.select_contact_by_id(contact.id)
        self.select_add_to_group(group)
        self.press_add_to_group()
        self.app.open_home_page()

    def remove_contact_from_group(self, contact, group):
        self.app.open_home_page()
        self.select_contacts_in_group(group)
        self.select_contact_by_id(contact.id)
        self.submit_remove()
        self.app.open_home_page()
