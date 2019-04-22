from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
import unittest


class CompareProducts(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.get("http://demo.magentocommerce.com")

		search_filed = self.driver.find_element_by_name("q")
		search_filed.clear()
		search_filed.send_keys("phones")
		search_filed.submit()

		self.driver.find_element_by_link_text("Add to Compare").click()
		clear_all_link = WebDriverWait(self.driver, 10).\
			until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Clear All")))
		clear_all_link.click()

		alert = WebDriverWait(self.driver, 10).until(expected_conditions.alert_is_present())
		alert_text = alert.text

		self.assertEqual("Are you sure you would like to remove all products from your comparison?", alert_text)
		alert.accept()

	def tearDown(self):
		self.driver.quit()


if __name__ == "__main__":
	unittest.main(verbosity=2)

