
Feature: Login functionality

  Scenario: Successful login
    Given user is on saas login page
    When user enters username
    And user enters password
    And user clicks login button
    Then user should be logged in successfully

  Scenario: Login without username
    Given user is on saas login page
    When user enters password
    And user clicks login button
    Then user should see username required error

 