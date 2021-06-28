from selenium.webdriver.support.select import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def open_edit_page(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//img[@alt='Edit']").click()

    def accept_alert(self):
        wd = self.app.wd
        wd.switch_to_alert().accept()

    def submit_delete(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def submit_update(self):
        wd = self.app.wd
        wd.find_element_by_name("update").click()

    def submit_enter(self):
        wd = self.app.wd
        wd.find_element_by_name("submit").click()

    def return_to_add_new_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def fill_contact(self, entry):
        wd = self.app.wd
        # fill in first name
        if entry.firstname:
            wd.find_element_by_name("firstname").click()
            wd.find_element_by_name("firstname").clear()
            wd.find_element_by_name("firstname").send_keys(entry.firstname)
        # fill in middle name
        if entry.middlename:
            wd.find_element_by_name("middlename").clear()
            wd.find_element_by_name("middlename").send_keys(entry.middlename)
        # fill in last name
        if entry.lastname:
            wd.find_element_by_name("lastname").clear()
            wd.find_element_by_name("lastname").send_keys(entry.lastname)
        # fill in nickname
        if entry.nickname:
            wd.find_element_by_name("nickname").clear()
            wd.find_element_by_name("nickname").send_keys(entry.nickname)
        # pass path to photo
        if entry.photo:
            wd.find_element_by_name("photo").clear()
            wd.find_element_by_name("photo").send_keys(entry.photo)
        # fill in title
        if entry.title:
            wd.find_element_by_name("title").click()
            wd.find_element_by_name("title").clear()
            wd.find_element_by_name("title").send_keys(entry.title)
        # fill in company
        if entry.company:
            wd.find_element_by_name("company").click()
            wd.find_element_by_name("company").clear()
            wd.find_element_by_name("company").send_keys(entry.company)
        # fill in address
        if entry.address:
            wd.find_element_by_name("address").click()
            wd.find_element_by_name("address").clear()
            wd.find_element_by_name("address").send_keys(entry.address)
        # fill in home phone
        if entry.t_home:
            wd.find_element_by_name("home").click()
            wd.find_element_by_name("home").clear()
            wd.find_element_by_name("home").send_keys(entry.t_home)
        # fill in mobile phone
        if entry.t_mobile:
            wd.find_element_by_name("mobile").clear()
            wd.find_element_by_name("mobile").send_keys(entry.t_mobile)
        # fill in work phone
        if entry.t_work:
            wd.find_element_by_name("work").clear()
            wd.find_element_by_name("work").send_keys(entry.t_work)
        # fill in fax
        if entry.t_fax:
            wd.find_element_by_name("fax").clear()
            wd.find_element_by_name("fax").send_keys(entry.t_fax)
        # fill in email
        if entry.email:
            wd.find_element_by_name("email").click()
            wd.find_element_by_name("email").clear()
            wd.find_element_by_name("email").send_keys(entry.email)
        # Fill in email2 #########
        if entry.email2:
            wd.find_element_by_name("email2").click()
            wd.find_element_by_name("email2").clear()
            wd.find_element_by_name("email2").send_keys(entry.email2)
        # Fill in email3 #####
        if entry.email3:
            wd.find_element_by_name("email3").clear()
            wd.find_element_by_name("email3").send_keys(entry.email3)
        # Fill in homepage
        if entry.homepage:
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
        if entry.secondary:
            if entry.secondary.address:
                wd.find_element_by_name("address2").click()
                wd.find_element_by_name("address2").clear()
                wd.find_element_by_name("address2").send_keys(entry.secondary.address)
            # Enter secondary phone
            if entry.secondary.home:
                wd.find_element_by_name("phone2").click()
                wd.find_element_by_name("phone2").clear()
                wd.find_element_by_name("phone2").send_keys(entry.secondary.home)
            # Add notes
            if entry.secondary.notes:
                wd.find_element_by_name("notes").clear()
                wd.find_element_by_name("notes").send_keys(entry.secondary.notes)

    def create(self, entry):
        self.open_add_new_page()
        self.fill_contact(entry)
        self.submit_enter()
        self.open_add_new_page()

    def modify_first_contact(self, entry):
        self.app.open_home_page()
        self.select_first_contact()
        self.open_edit_page()
        self.fill_contact(entry)
        self.submit_update()
        self.app.open_home_page()

    def delete_first_contact(self):
        self.app.open_home_page()
        self.select_first_contact()
        self.submit_delete()
        self.accept_alert()
        self.app.open_home_page()

    def delete_first_contact_via_edit(self):
        self.app.open_home_page()
        self.select_first_contact()
        self.open_edit_page()
        self.submit_delete()
        self.app.open_home_page()
