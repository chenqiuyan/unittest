import unittest
from appium import webdriver


class SearchProductsOnIPhone(unittest.TestCase):
	def setUp(self):
		desired_caps = {}
		desired_caps['device'] = 'Android'
		desired_caps['version'] = '4.3'
		desired_caps['app'] = 'Chrome'

		self.driver = webdriver.Remote("http://127.0.1.1:4723/wd/hub", desired_caps)
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
