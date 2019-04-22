import unittest
from appium import webdriver


class SearchProductsOnIPhone(unittest.TestCase):
	SAUCE_USERNAME = "upgundecha"
	SUACE_KEY = "c6e7132c-ae27-4217-b6fa-3cf7df0a7182"

	def setUp(self):
		desired_caps = {}
		desired_caps['browserName'] = "Safari"
		desired_caps["platformVersion"] = "7.1"
		desired_caps["platformName"]  = "iOS"
		desired_caps["deviceName"] = "iPhone Simulator"

		sauce_string = self.SAUCE_USERNAME + ":" + self.SUACE_KEY

		self.driver = webdriver.Remote("http://" + sauce_string + "@ondemand.saucelabs.com:80/wd/hub", desired_caps)
		self.driver.get("http://demo.magentocommerce.com/")
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()

	def test_search_by_category(self):
		self.driver.find_element_by_xpath("//a[@href='#header-search']").click()
		self.search_field = self.driver.find_element_by_name("q")
		self.search_field.clear()
		self.search_field.send_keys("phones")
		self.search_field.submit()

		products = self.driver.find_element_by_xpath("//div[@class='category-products']/ul/li")

		self.assertEqual(2, len(products))

	def tearDown(self):
			self.driver.quit()


if __name__ == "__main__":
	unittest.main(verbosity=2)
