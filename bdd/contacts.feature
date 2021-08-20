Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <middlename>, <lastname>, <nickname>, <title>, <company>, <address>, <home>, <mobile>, <work>, <fax>, <email>, <email2>, <email3>, <homepage>, <address2>, <phone2>, <notes>, <bday>, <bmonth>, <byear>, <aday>, <amonth> and <ayear>
  When I add the contact to the list
  Then the new contact list is equal to the old list with the added new contact

  Examples:
  | firstname   | middlename   | lastname   | nickname   | title   | company   |  address   | home   | mobile    |  work     | fax     | email             | email2            | email3            | homepage       |address2 |  phone2    | notes  |bday| bmonth   |  byear |aday| amonth  | ayear |
  | firstname1  | middlename1  | lastname1  | nickname1  | title1  | company1  |  address1  | home1  | 12345678  |  12345678 | 12345678| u1_email@localhost| u1_email@localhost| u1_email@localhost| https://hp.ru  | address2  |  123456  | notes  | 1  | 1        |  1980  | 1  | 1       | 2001  |
  | firstname2  | middlename2  | lastname2  | nickname2  | title2  | company2  |  address2  | home2  | 12345678  |  12345678 | 12345678| u2_email@localhost| u2_email@localhost| u2_email@localhost| https://hp.ru  | address2  |  123456  | notes  | 2  | 1        |  1981  | 2  | 1       | 2002  |


Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old contact list without the deleted contact


Scenario Outline: Modify a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <firstname>, <middlename>, <lastname>, <nickname>, <title>, <company>, <address>, <home>, <mobile>, <work>, <fax>, <email>, <email2>, <email3>, <homepage>, <address2>, <phone2>, <notes>, <bday>, <bmonth>, <byear>, <aday>, <amonth> and <ayear>
  When I modify the contact from the list
  Then the new contact list is equal to the old contact list with the modified contact

  Examples:
  | firstname   | middlename   | lastname   | nickname   | title   | company   |  address   | home   | mobile    |  work     | fax     | email             | email2            | email3            | homepage       |address2 |  phone2    | notes  |bday| bmonth   |  byear |aday| amonth  | ayear |
  | firstname1  | ChangeNew2  | lastname_changed | nickname1  | title1  | company1  |  address_changed  | home1  | 12345678  |  12345678 | 12345678| u1_email@localhost| u1_email@localhost| u1_email@localhost| https://hp.ru  | address2  |  123456  | notes  | 1  | 02  |  1980  | 1  | 05 | 2001  |
