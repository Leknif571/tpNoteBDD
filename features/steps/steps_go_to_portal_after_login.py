from behave import given, when, then
from time import sleep

@given(u'I am on the login page')
def step_impl(self):
    url = self.driver.current_url
    self.tc.assertEqual(url, "http://localhost/login.php")


@when(u'I complete the login form with valid credentials')
def step_impl(self):
    self.driver.find_element(self.by.ID, "login").send_keys("bee")
    self.driver.find_element(self.by.ID, "password").send_keys("bug")


@when(u'I click on the "Login" button')
def step_impl(self):
    self.driver.find_element(self.by.TAG_NAME, "button").click()
    sleep(1)

@then(u'I should be redirected to the portal page')
def step_impl(self):
    url = self.driver.current_url
    self.tc.assertEqual(url, "http://localhost/portal.php")
