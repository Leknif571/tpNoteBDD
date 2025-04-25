#  Login réussite (Pour bWapp, login "bee", password "bug"

Feature: Go to portal after login with connect credential
  Scenario: Redirect to portal after login with connect credential
    Given I am on the login page
    When I complete the login form with valid credentials
    And I click on the "Login" button
    Then I should be redirected to the portal page
