from behave import given, when, then


@then(u'I should see the "Security Level" input form')
def step_impl(self):
    security_level_text = self.driver.find_element(self.by.ID, 'security_level').is_displayed()
    self.tc.assertTrue(security_level_text, "Security Level input form is not displayed")

@when(u'I select the "Security Level" in the select form')
def step_impl(self):
    security_level_select = self.driver.find_element(self.by.ID, 'security_level')
    security_level_select.click()
    security_level_select.send_keys("High")

@when(u'I click on the "set" button')
def step_impl(self):
    self.driver.find_element(self.by.XPATH, "//*[@id='main']/form/button").click()
    self.tc.assertTrue(self.driver.find_element(self.by.XPATH, "//*[@id='main']/font").is_displayed(), "Success message is not displayed")      


@then(u'I should see a the text change with the new security level')
def step_impl(self):
    success_message = self.driver.find_element(self.by.XPATH, '//*[@id="main"]/font').text
    self.tc.assertEqual(success_message, "Security Level set to High")

@then(u'I should stay on the portal page')
def step_impl(self):
    url = self.driver.current_url
    self.tc.assertEqual(url, "http://localhost/portal.php")