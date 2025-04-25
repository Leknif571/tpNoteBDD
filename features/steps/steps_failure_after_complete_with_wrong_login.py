from behave import given, when, then

@when(u'I complete the input login form with invalid credentials')
def step_impl(self):
    self.driver.find_element(self.by.ID, "login").send_keys("biz")

@when(u'I complete the input password form with invalid credentials')
def step_impl(self):
    self.driver.find_element(self.by.ID, "password").send_keys("buz")

@then(u'I should see an error message')
def step_impl(self):
    error_message = self.driver.find_element(self.by.XPATH, '//*[@id="main"]/font').text
    self.tc.assertEqual(error_message, "Invalid credentials or user not activated!")