# https://behave.readthedocs.io/en/latest/tutorial.html#python-step-implementations
# https://jenisys.github.io/behave.example/tutorials/tutorial03.html

Feature: Step parameters
  Goal:	Use step parameter to handover parameters to step functions.

Scenario: look up a book
  Given I search for a valid book
   Then the result page will include "success"

Scenario: look up an invalid book
  Given I search for a invalid book
   Then the result page will include "failure"