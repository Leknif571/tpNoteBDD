    # - Changement de mot de passe (après s'être connecté)

Feature: Change password after connected
  Scenario: Change password after connected
    Given I am on the login page
    When I complete the login form with valid credentials
    And I click on the "Login" button
    Then I should be redirected to the portal page
    When I click on the "Change Password" link
    Then I am redirected to the change password page
    When I complete the input current password form with valid credentials
    And I complete the input new password form with valid credentials
    And I complete the input confirm password form with valid credentials
    And I click on the "Change Password" button
    Then I should see a success message "The password has been changed!"
    And I should stay on the change password page
