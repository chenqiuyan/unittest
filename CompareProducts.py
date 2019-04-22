from selenium import webdriver
import unittest


class CompareProducts(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()

		self.driver.get("http://demo.magentocommerce.com")

	def test_compare_products_removal_alert(self): # 搜索产品并添加到比较列表
		search_field = self.driver.find_element_by_name("q")
		search_field.clear()
		search_field.send_keys("phones")
		search_field.submit()
		self.driver.find_element_by_link_text("Add to Compare").click()

		# 读取并检验警告信息是都正确
		self.driver.find_element_by_link_text("Clear All").click()
		alert = self.driver.switch_to.alert()
		alert_text = alert.text
		self.assertEqual("Are you sure you would like to remove all products from your comparison?", alert_text)
		alert.accept()

	def tearDown(self):
		self.driver.quit()


if __name__ == "__main__":
	unittest.main(verbosity=2)


