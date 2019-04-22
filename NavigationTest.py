import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class NavigationTest(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()
		self.driver.get("https://www.baidu.com/")

	def testBrowserNavigation(self):
		driver = self.driver
		search_field = driver.find_element_by_name("wd")
		search_field.clear()

		search_field.send_keys("selenium webdriver")
		search_field.submit()

		se_wd_link = driver.find_element_by_link_text("Selenium Webdriver")
		se_wd_link.click()
		self.assertEqual("Selenium Webdriver", driver.title)

		driver.back()
		self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is("Selenium webdriver - Google Search")))

		driver.forward()
		self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is("Selenium Webdriver")))

		driver.refresh()
		self.assertTrue(WebDriverWait(self.driver, 10).until(expected_conditions.title_is("Selenium Webdriver")))

	def tearDown(self):
		self.driver.quit()


if __name__ == "__main__":
	unittest.main(verbosity=2)
