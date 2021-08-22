
Scenario Outline: Add new group
  Given a group list
  Given a group with <name>, <header> and <footer>
  When I add the group to the list
  Then the new group list is equal to the old group list with added new group

  Examples:
  |   name   |   header   |   footer   |
  | new-name1 | new_header2 | new_footer3 |


Scenario: Delete a group
  Given a non-empty group list
  Given a random group from the list
  When I delete the group from the list
  Then the new group list is equal to the old group list without the deleted group


Scenario Outline: Modify a group
  Given a non-empty group list
  Given a random group from the list
  Given a group with <name>, <header> and <footer>
  When I modify the group from the list
  Then the new group list is equal to the old group list with the modified group

  Examples:
  |   name   |   header   |   footer   |
  | new name | new header | new footer |

