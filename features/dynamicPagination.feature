Feature: Dynamic Pagination Table Validations

  Scenario: Validate row count based on dropdown
    Given I navigate to pagination table page
    When I select 5 entries from dropdown
    Then I should see 5 rows in the table

  Scenario: Validate entries text
    Given I navigate to pagination table page
    When I select 5 entries from dropdown
    Then I should see entries text updated correctly

  
  
  Scenario: Validate sorting on Student Name column
    Given I navigate to pagination table page
    When I select 10 entries from dropdown
    When I sort Student Name column
    Then the column should be sorted correctly

  Scenario: Validate sorting on Student Name column
    Given I navigate to pagination table page
    When I select 10 entries from dropdown
    When I sort Student Name column
    Then the column should be sorted correctly

  Scenario: Validate sorting on Student Name column
    Given I navigate to pagination table page
    When I search for Bob Williams
    Then only matching records should be displayed
    And pagination buttons should be disabled
