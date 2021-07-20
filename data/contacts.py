from model.contact import Contact
from model.secondary import Secondary


testdata = [
    Contact(firstname="f1", middlename="md1", lastname="ln1",
             nickname="nn1", photo=None, title="t1",
             company="cmp1", address="adrs1",
             t_home="4(567)77878", t_mobile="33333", t_work="2222",
             t_fax="",
             email="empty@email.com", email2="", email3="", homepage="",
             birthdate=None, anniversary=None,
             secondary=Secondary("", "", ""))
]