from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest


class ExplicitWaitTests(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://demo.magentocommerce.com")

	def test_account_link(self):
		WebDriverWait(self, 10).\
			until(lambda s: s.find_element_by_id("select-language").get_attribute("length") == "3")
		account = WebDriverWait(self, 10).\
			until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "ACCOUNT")))
		account.click()

	def tearDown(self):
		self.driver.quit()

	if __name__ == "__main__":
		unittest.main(verbosity=2)
