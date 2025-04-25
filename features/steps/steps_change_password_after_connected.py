from behave import given, when, then
from time import sleep

@when(u'I click on the "Change Password" link')
def step_impl(self):
    self.driver.find_element(self.by.LINK_TEXT, "Change Password").click()
    sleep(1)

@then(u'I am redirected to the change password page')
def step_impl(self):
    url = self.driver.current_url
    self.tc.assertEqual(url, "http://localhost/password_change.php")

@when(u'I complete the input current password form with valid credentials')
def step_impl(self):
    self.driver.find_element(self.by.ID, "password_curr").send_keys("bug")

@when(u'I complete the input new password form with valid credentials')
def step_impl(self):
    self.driver.find_element(self.by.ID, "password_new").send_keys("bug")

@when(u'I complete the input confirm password form with valid credentials')
def step_impl(self):
    self.driver.find_element(self.by.ID, "password_conf").send_keys("bug")

@when(u'I click on the "Change Password" button')
def step_impl(self):
    self.driver.find_element(self.by.XPATH, "//*[@id='main']/form/button").click()
    sleep(1)

@then(u'I should see a success message "The password has been changed!"')
def step_impl(self):
    success_message = self.driver.find_element(self.by.XPATH, '//*[@id="main"]/font').text
    self.tc.assertEqual(success_message, "The password has been changed!")

@then(u'I should stay on the change password page')
def step_impl(self):
    url = self.driver.current_url
    self.tc.assertEqual(url, "http://localhost/password_change.php")