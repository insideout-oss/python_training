# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import datetime
from secondary import Secondary
from entry import Entry


class AddAddressBookEntry(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
    
    def test_add_address_book_entry(self):
        wd = self.driver
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_add_new_page(wd)
        self.fill_in_new_entry(wd, Entry(firstname="Irina", middlename="MiddleName", lastname="LastName",
                                         nickname="insideout-oss", photo="C:\\fakepath\\Screenshot.png", title="Mrs.",
                                         company="companyX", address="addressX",
                                         t_home="888888888", t_mobile="87777777777", t_work="567890987",
                                         t_fax="567890987",
                                         email="test email", email2="", email3="", homepage="https://homepage.it",
                                         birthdate=datetime.date(1999, 10, 8), anniversary=datetime.date(2000, 12, 29),
                                         secondary=Secondary("second address", "home phone", "notes")))
        self.return_to_add_new_page(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def test_add_empty_address_book_entry(self):
        wd = self.driver
        self.open_home_page(wd)
        self.login(wd, "admin", "secret")
        self.open_add_new_page(wd)
        self.fill_in_new_entry(wd, Entry(firstname="", middlename="", lastname="",
                                         nickname="", photo="", title="",
                                         company="", address="",
                                         t_home="", t_mobile="", t_work="",
                                         t_fax="",
                                         email="", email2="", email3="", homepage="",
                                         birthdate=None, anniversary=None,
                                         secondary=Secondary("", "", "")))
        self.return_to_add_new_page(wd)
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        wd.find_element_by_link_text("home").click()

    def return_to_add_new_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def fill_in_new_entry(self, wd, entry):
        # fill in first name
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(entry.firstname)
        # fill in middle name
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(entry.middlename)
        # fill in last name
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(entry.lastname)
        # fill in nickname
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(entry.nickname)
        # DO NOT WORK
        # wd.find_element_by_name("photo").click()
        # wd.find_element_by_name("photo").clear()
        # wd.find_element_by_name("photo").send_keys(entry.photo)
        # fill in title
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(entry.title)
        # fill in company
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(entry.company)
        # fill in address
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(entry.address)
        # fill in home phone
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(entry.t_home)
        # fill in mobile phone
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(entry.t_mobile)
        # fill in work phone
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(entry.t_work)
        # fill in fax
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(entry.t_fax)
        # fill in email
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(entry.email)
        # Fill in email2 #########
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(entry.email2)
        # Fill in email3 #####
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(entry.email3)
        # Fill in homepage
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(entry.homepage)
        # Select b-day
        if entry.birthdate:
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(str(entry.birthdate.day))
            wd.find_element_by_xpath("//option[@value='" + str(entry.birthdate.day) + "']").click()
            # Select b-month
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(entry.birthdate.strftime("%B"))
            wd.find_element_by_xpath("//option[@value='" + entry.birthdate.strftime("%B") + "']").click()
            # Select b-year
            wd.find_element_by_name("byear").click()
            wd.find_element_by_name("byear").clear()
            wd.find_element_by_name("byear").send_keys(str(entry.birthdate.year))
        # Select anniversary date
        if entry.anniversary:
            wd.find_element_by_name("aday").click()
            Select(wd.find_element_by_name("aday")).select_by_visible_text(str(entry.anniversary.day))
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option["+str(entry.anniversary.day + 2)+"]").click()
            wd.find_element_by_name("amonth").click()
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(str(entry.anniversary.strftime("%B")))
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option["+str(entry.anniversary.month + 1)+"]").click()
            # year
            wd.find_element_by_name("ayear").click()
            wd.find_element_by_name("ayear").clear()
            wd.find_element_by_name("ayear").send_keys(str(entry.anniversary.year))
        # Enter second address
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(entry.secondary.address)
        # Enter secondary phone
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(entry.secondary.home)
        # Add notes
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(entry.secondary.notes)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_add_new_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/index.php")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()



if __name__ == "__main__":
    unittest.main()
