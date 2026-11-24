Feature: File Upload and Download

  Scenario: Upload a file
    Given I navigate to upload page
    When I upload a file
    And I click on upload button
    Then File should be uploaded successfully
    And Uploaded file name should be displayed