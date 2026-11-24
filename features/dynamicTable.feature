Feature: Validate dynamic table CPU value

Scenario: Compare Chrome CPU value with label
    Given I navigate to the dynamic table page
    When I fetch CPU value for Chrome from the table
    