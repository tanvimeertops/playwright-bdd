Feature: Handle iframe and multiple windows

Scenario: Handle iframe and enter text
    Given I navigate to the iframe page
    When I enter text inside the iframe
    Then I should see the text entered
    
Scenario: Handle multiple windows
    Given I navigate to the windows page
    When I click on the "Click Here" link
    Then I should switch to new window and validate content
    And I close the child window and switch back to parent