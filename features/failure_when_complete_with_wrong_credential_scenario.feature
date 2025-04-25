    # - Login échec anticipé (mauvais identifiant et password)

Feature: Failure when complete with wrong credential
  Scenario: Display error message when login with invalid credentials
    Given I am on the login page
    When I complete the input login form with invalid credentials
    And  I complete the input password form with invalid credentials
    And I click on the "Login" button
    Then I should see an error message



