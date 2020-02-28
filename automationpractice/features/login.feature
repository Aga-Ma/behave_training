Feature: Login to portal

  Scenario: Login and logout
    When I open automationpractice website
    And I login with username "baxome2199@kamismail.com" and password "poiuytrewq123"
    Then I verify that I successfully logged in by logging out