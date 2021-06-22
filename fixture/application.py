from selenium import webdriver
from selenium.webdriver.support.select import Select
from fixture.session import SessionHelper


class Application:

    def __init__(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)
        self.session = SessionHelper(self)

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/index.php")

    def open_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def return_to_groups_page(self):
        wd = self.wd
        wd.find_element_by_link_text("groups").click()

    def create_group(self, group):
        wd = self.wd
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

    def open_add_new_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def fill_in_new_entry(self, entry):
        wd = self.wd
        self.open_add_new_page()
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
        # pass path to photo
        if entry.photo:
            wd.find_element_by_name("photo").clear()
            wd.find_element_by_name("photo").send_keys(entry.photo)
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
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option["+str(entry.anniversary.day + 2)+"]").\
                click()
            wd.find_element_by_name("amonth").click()
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(str(entry.anniversary.strftime("%B")))
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option["+str(entry.anniversary.month + 1)+"]").\
                click()
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
        self.return_to_add_new_page()

    def return_to_add_new_page(self):
        wd = self.wd
        wd.find_element_by_link_text("add new").click()

    def destroy(self):
        self.wd.quit()

