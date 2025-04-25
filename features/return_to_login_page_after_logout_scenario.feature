    # - Logout (donc initialement être loggé)

Feature: Return to login page after logout scenario

  Scenario: Return to login page after logout
    Given I am on the login page
    When I complete the login form with valid credentials
    And I click on the "Login" button
    Then I should be redirected to the portal page
    When I click on the "Logout" button
    Then I should see alert message "Are you sure you want to leave?"
    When I click on the "OK" button in the alert message
    Then I should be redirected to the login page    
