# https://behave.readthedocs.io/en/latest/tutorial.html#python-step-implementations
# https://jenisys.github.io/behave.example/tutorials/tutorial03.html

Feature: Step parameters
  Goal:	Use step parameter to handover parameters to step functions.

  Scenario: Blenders
    Given I put "apples" in a blender
    When I switch the blender on
    Then it should transform into "apple juice"