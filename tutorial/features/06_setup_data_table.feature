# Associating a table of data with a step
# https://jenisys.github.io/behave.example/tutorials/tutorial06.html

Feature: Step setup table

Scenario: Setup table
  Given a set of specific users
    | name      | department  |
    | Barry     | Beer Cans   |
    | Pudey     | Silly Walks |
    | Two-Lumps | Silly Walks |
  When we count the number of people in each department
  Then we will find two people in "Silly Walks"
   But we will find one person in "Beer Cans"
