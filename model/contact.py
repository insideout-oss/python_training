from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None,
                 photo=None, title=None, company=None, address=None,
                 t_home=None, t_mobile=None, t_work=None, t_fax=None,
                 email=None, email2=None, email3=None, homepage=None,
                 birthdate=None, anniversary=None, secondary=None, id=None,
                 all_phones_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.photo = photo
        self.title = title
        self.company = company
        self.address = address
        self.t_home = t_home
        self.t_mobile = t_mobile
        self.t_work = t_work
        self.t_fax = t_fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthdate = birthdate
        self.anniversary = anniversary
        self.secondary = secondary
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
               (self.firstname is None or self.firstname == other.firstname) and \
               (self.lastname is None or self.lastname == other.lastname)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

