    # - Modifier le niveau de sécurité (après s'être connecté)
Feature: Change security level after connected
  Scenario: Change security level after connected
    Given I am on the login page
    When I complete the login form with valid credentials
    And I click on the "Login" button
    Then I should be redirected to the portal page
    And I should see the "Security Level" input form
    When I select the "Security Level" in the select form
    And I click on the "set" button
    Then I should see a the text change with the new security level
    And I should stay on the portal page

