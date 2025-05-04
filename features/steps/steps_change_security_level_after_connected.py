from behave import given, when, then
from time import sleep 


@then(u'I should see the "Security Level" input form')
def step_impl(self):
    security_level_text = self.driver.find_element(self.by.ID, 'security_level').is_displayed()
    self.tc.assertTrue(security_level_text, "Security Level input form is not displayed")

@when(u'I select the "Security Level" in the select form')
def step_impl(self):
    security_level_select = self.driver.find_element(self.by.NAME, 'security_level')
    select = self.Select(security_level_select)
    select.select_by_value('2')
    self.tc.assertEqual(security_level_select.get_attribute('value'), '2', "Security Level is not set to High")

@when(u'I click on the "set" button')
def step_impl(self):
    self.driver.find_element(self.by.XPATH, "//*[@id='security_level']/form/button").click()


@then(u'I should see a the text change with the new security level')
def step_impl(self):
    self.tc.assertTrue(self.driver.find_element(self.by.XPATH, "//*[@id='security_level']/form/font/b").is_displayed(), "high")      

@then(u'I should stay on the portal page')
def step_impl(self):
    url = self.driver.current_url
    self.tc.assertEqual(url, "http://localhost/portal.php")