Feature: Add product to cart

    Scenario: Verify address and verify shipping address
    When I open automationpractice website
    And I login with username "baxome2199@kamismail.com" and password "poiuytrewq123"
    And I hover on women menu item and click summer dresses
    And I add a summer dress to cart
    And verify the item and price
    And I verify the address and proceed
    Then I verify shipping address and proceed