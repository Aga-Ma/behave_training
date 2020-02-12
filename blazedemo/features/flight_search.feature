@fixture.browser.chrome
Feature: The user can book available flights

  Scenario: the user can find flight from Paris to London
    Given the user is on search page
    When user selects Paris as departure city
    And user selects London as destination city
    And clicks on Find Flights button
