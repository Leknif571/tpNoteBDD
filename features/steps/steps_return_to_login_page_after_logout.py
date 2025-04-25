from behave import given, when, then
from time import sleep

@when(u'I click on the "Logout" button')
def step_impl(self):
    self.driver.find_element(self.by.LINK_TEXT, "Logout").click()
    sleep(1)

@then(u'I should see alert message "Are you sure you want to leave?"')
def step_impl(self):
    alert_message = self.driver.switch_to.alert.text
    self.tc.assertEqual(alert_message, "Are you sure you want to leave?")

@when(u'I click on the "OK" button in the alert message')
def step_impl(self):
    self.driver.switch_to.alert.accept()
    sleep(1)

@then(u'I should be redirected to the login page')
def step_impl(self):
    url = self.driver.current_url
    self.tc.assertEqual(url, "http://localhost/login.php")