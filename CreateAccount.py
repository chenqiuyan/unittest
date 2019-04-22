from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest


class RegisterNewUser(unittest.TestCase): # 创建一个新的测试类，并实例化
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()

		self.driver.get("http://demo.magentocommerce.com")

	def test_register_new_user(self):
		driver = self.driver
		driver.find_element_by_link_text("Log In").click()
		# 检查创建新用户的按钮对于用户是否可见并可用
		create_account_button = driver.find_element_by_link_text("//button[@title='Create an Account']")
		self.assertTrue(create_account_button.is_displayed() and create_account_button.is_enabled())

		# 使用title属性检验打开页面是否符合预期结果
		create_account_button.click()
		self.assertEqual("Create New Customer Account - Magento Commerce Demo Store", driver.title)

		# 定位页面的所有元素
		first_name = driver.find_element_by_id("firstname")
		last_name = driver.find_element_by_id("lastname")
		email_address = driver.find_element_by_id("email_address")
		news_letter_subscription = driver.find_element_by_id("is_subscibed") # newsletter subscription 邮件订阅
		password = driver.find_element_by_id("password")
		confirm_password = driver.find_element_by_id("confirmation")
		submit_button = driver.find_element_by_xpath("//button[@title='Submit']")

		# get_attribute()方法可以用来获取元素的属性值，校验文本框的最大字符限制，字符限制就是通过maxlength属性来实现
		# 把属性名称当作参数传递给get_attribute()方法
		self.assertEqual("255", first_name.get_attribute("maxlength"))

		# 确保所有的字段对于用户都是可见和可用的
		self.assertTrue(first_name.is_enabled() and last_name.is_enabled() and password.is_enabled()
						and email_address.is_enabled() and news_letter_subscription.is_enabled()
						and confirm_password.is_enabled() and submit_button.is_enabled())

		# 检查Sign UP for Newsletter 复选框是否---默认"不被选中"
		self.assertFalse(news_letter_subscription.is_selected())

		# 检验欢迎信息来检查用户是否被创建成功以及注销是否可见
		self.assertEqual("Hello, Test User1!", driver.find_element_by_css_selector("p.hello > strong").text)
		self.assertTrue(driver.find_element_by_link_text("LogOut").is_displayed())

		def test_create_new_customer(self): # 判断某个元素是否存在
			self.driver.find_elmement_by_link_text("ACCOUNT").click()
			my_account = WebDriverWait(self.webdriver, 10).\
				until(expected_conditions.element_to_be_clickable((By.LINK_TEXT, "My Account")))
			create_account_button.click()
			WebDriverWait(self.driverm, 10).until(expected_conditions.title_contains("Create New Customer Account"))

		def test_LoginLink(self):
			WebDriverWait(self.driver, 10).\
				until(lambda s: s.find_element_by_id("select-language").get_attribute("length") == "3")
			login_link = WebDriverWait(self.driver, 10).\
				until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Log In")))
			login_link.click()

	def tearDown(self):
		self.driver.quit()


# unittest是python自带的单元测试包。其实相当于java中的junit。意思就是运行不需要再写主函数调用
# verbosity 信息复杂度,2 (详细模式):测试结果会显示每个测试用例的所有相关的信息
if __name__ == "__main__":
	unittest.main(verbosity=2)












