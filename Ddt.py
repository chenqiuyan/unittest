import unittest
import time
from ddt import ddt, data, unpack
from selenium import webdriver


@ddt  # 在测试类中使用@ddt装饰符
class SearchDDT(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()

		self.driver.get("https://baidu.com/")

	# 在测试方法中使用@data:把参数当作测试数据，参数可以是单个值，列表，元祖，字典
	@data(("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh", 7), ("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh1", 10))
	# @unpack 装饰符把元祖和列表解析成多个参数
	@unpack
	# 在方法中，value和excepted_count两个参数用来接收元祖解析的数据
	def test_search_ddt(self, value, expected_count):
		self.search_field = self.driver.find_element_by_id("kw")
		self.search_field.clear()
		self.search_field.send_keys(value)
		self.search_field.submit()
		time.sleep(6)

		items = list(self.driver.find_elements_by_xpath("//h3[@class='t']"))
		self.assertEqual(expected_count, len(items))

	def tearDown(self):
		self.driver.quit()


if __name__ == "__main__":
	unittest.main()




