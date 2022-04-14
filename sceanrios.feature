Feature: Automate website for interview


  Scenario: I want to navigate to way2automation and add user
    Given I go to the site "way2automation" website
    And Verify page "pagetitle" is present
    When I click on "adduser" button
    Then Verify "savebutton" is disabled and "closebutton" is enabled
    Then Enter "FirstName" "LastName" "UserName" "Password" "Email" and "CellPhone"
    Then Select Role
    Then I click on "save" button
    And Verify "UserName" is displayed

  Scenario: I want to delete user Novak from way2automation
    Given I go to the site "way2automation" website
    And Verify page "pagetitle" is present
    Then Search for user "DeleteUsername" on homepage and click on "deletebutton"
    Then Click on "OKbutton" from deletescreen
    And Verify "DeleteUsername" is deleted

