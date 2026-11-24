Feature: Drag and Drop Actions

  Scenario: Drag Box A to Box B
    Given I navigate to drag and drop page
    When I drag box A to box B
    Then Box A header should change to B

Scenario: Drag circles into target box
    Given I navigate to drag drop circles page
    When I drag red circle into target
    And I drag green circle into target
    And I drag blue circle into target
    Then All circles should be inside target box