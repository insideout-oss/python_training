# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest


class AddAddressBookEntry(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
    
    def test_add_address_book_entry(self):
        driver = self.driver
        # open home page
        driver.get("http://localhost/addressbook/index.php")
        # login
        driver.find_element_by_name("user").click()
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys("admin")
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys("secret")
        driver.find_element_by_xpath("//input[@value='Login']").click()
        # open "add new" page
        driver.find_element_by_link_text("add new").click()
        # fill in new entry
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys("Irina")
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys("MiddleName")
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys("LastName")
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys("insideout-oss")
        driver.find_element_by_name("title").click()
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys("title")
        driver.find_element_by_name("company").click()
        driver.find_element_by_name("company").clear()
        driver.find_element_by_name("company").send_keys("company")
        driver.find_element_by_name("address").click()
        driver.find_element_by_name("address").clear()
        driver.find_element_by_name("address").send_keys("address")
        driver.find_element_by_name("home").click()
        driver.find_element_by_name("home").clear()
        driver.find_element_by_name("home").send_keys("888888888")
        driver.find_element_by_name("mobile").clear()
        driver.find_element_by_name("mobile").send_keys("87777777777")
        driver.find_element_by_name("work").clear()
        driver.find_element_by_name("work").send_keys("567890987")
        driver.find_element_by_name("fax").clear()
        driver.find_element_by_name("fax").send_keys("567890987")
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys("irina.bezruk@gmail.com")
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text("1")
        driver.find_element_by_xpath("//option[@value='1']").click()
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text("January")
        driver.find_element_by_xpath("//option[@value='January']").click()
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys("1999")
        driver.find_element_by_name("aday").click()
        Select(driver.find_element_by_name("aday")).select_by_visible_text("1")
        driver.find_element_by_xpath("//div[@id='content']/form/select[3]/option[3]").click()
        driver.find_element_by_name("amonth").click()
        Select(driver.find_element_by_name("amonth")).select_by_visible_text("January")
        driver.find_element_by_xpath("//div[@id='content']/form/select[4]/option[2]").click()
        driver.find_element_by_name("new_group").click()
        driver.find_element_by_name("address2").click()
        driver.find_element_by_name("address2").clear()
        driver.find_element_by_name("address2").send_keys("second address")
        driver.find_element_by_name("phone2").click()
        driver.find_element_by_name("phone2").clear()
        driver.find_element_by_name("phone2").send_keys("home address")
        driver.find_element_by_name("notes").clear()
        driver.find_element_by_name("notes").send_keys("notes")
        driver.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # return to "add new" page
        driver.find_element_by_link_text("add new").click()
        # return to home page
        driver.find_element_by_link_text("home").click()
        # logout
        driver.find_element_by_link_text("Logout").click()

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
