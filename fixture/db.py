import pymysql
from model.group import Group
from model.contact import Contact
from model.secondary import Secondary


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, address, home, mobile, work, fax, "
                           "email, email2, email3, homepage, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, address,
                 t_home, t_mobile, t_work, t_fax, email, email2, email3, homepage, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename, lastname=lastname,
                                    address=address, t_home=t_home, t_mobile=t_mobile, t_work=t_work, t_fax=t_fax,
                                    email=email, email2=email2, email3=email3, homepage=homepage,
                                    secondary=Secondary(home=phone2)))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
