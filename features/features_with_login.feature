Feature: feature with login scenario  


Background: Background for all scenarios
    Given I am on the login page
    When I complete the login form with valid credentials
    And I click on the "Login" button
    Then I should be redirected to the portal page
    
# - Modifier le niveau de sécurité (après s'être connecté)

  Scenario: Change security level after connected
    And I should see the "Security Level" input form
    When I select the "Security Level" in the select form
    And I click on the "set" button
    Then I should see a the text change with the new security level
    And I should stay on the portal page


# - Logout (donc initialement être loggé)
  Scenario: Return to login page after logout
    When I click on the "Logout" button
    Then I should see alert message "Are you sure you want to leave?"
    When I click on the "OK" button in the alert message
    Then I should be redirected to the login page   

# - Changement de mot de passe (après s'être connecté)
  Scenario: Change password after connected
    When I click on the "Change Password" link
    Then I am redirected to the change password page
    When I complete the input current password form with valid credentials
    And I complete the input new password form with valid credentials
    And I complete the input confirm password form with valid credentials
    And I click on the "Change Password" button
    Then I should see a success message "The password has been changed!"
    And I should stay on the change password page

#  Login réussite (Pour bWapp, login "bee", password "bug"
  Scenario: Redirect to portal after login with connect credential

