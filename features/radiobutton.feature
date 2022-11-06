Feature: Radio button page

  Scenario: Selection radio button 2 on radio button page
    Given I am on Homepage
    When I click the Radio Button link
    And  I am redirected to the Radio Button page
    And I click Radio button 2
    Then Radio button 2 is selected


