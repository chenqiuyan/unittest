import unittest
import time
import select
from selenium import webdriver


class HomePageTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		cls.driver = webdriver.Chrome()
		cls.driver.implicitly_wait(30)
		cls.driver.maximize_window()

		cls.driver.get("http://demo.magentocommerce.com")

	def test_search_field_max_length(self):  # 检验搜索框的最大长度
		search_field = self.driver.\
			find_element_by_id("search")
		time.sleep(2)
		self.assertEqual("128", search_field.get_attribute("maxlength"))

	def test_search_button_enabled(self): # 检验搜索按钮是否可用
		search_button = self.driver.\
			find_element_by_class_name("button")
		time.sleep(2)
		self.assertTrue(search_button.is_enabled())

	def test_my_account_link_is_displayed(self):  # 检验我的账户是否可见
		account_link = \
			self.driver.find_element_by_link_text("ACCOUNT")
		time.sleep(2)
		self.driver.find_element_by_css_selector("div.header-minicart span.icon")
		time.sleep(2)
		self.assertTrue(account_link.is_displayed())

	def test_account_links(self):  # 检验我的账户链接长度
		account_links = self.driver.\
			find_element_by_partial_link_text("ACCOUNT")
		time.sleep(2)
		self.assertTrue(2, len(account_links))

	def test_count_of_promo_banners_images(self):  # 检验广告的的数量
		banner_list = self.driver.\
			find_element_by_class_name("promos")
		time.sleep(2)
		banners = banner_list.find_element_by_tag_name("img")
		self.assertEqual(2, len(banners))

	def test_vip_promo(self):  # 校验会员是否可视，标题是否一样
		vip_promo = self.driver.find_element_by_xpath("//img[@alt='Shop Private Sales - Members Only']")
		time.sleep(2)
		self.assertTrue(vip_promo.is_displayed())
		vip_promo.click()
		self.assertEqual("VIP", self.driver.title)

	def test_shopping_cart_status(self):  # 校验购物车的图标的文本，购物车为空时的提示，点击图标
		shopping_cart_icon = self.driver.\
			find_element_by_css_selector("div.header-minicart span.icon")
		time.sleep(2)
		shopping_cart_icon.click()

		shopping_cart_status = self.driver.\
			find_element_by_css_selector("p.empty").text
		time.sleep(2)
		self.assertEqual("You have to items in your shopping cart.", shopping_cart_status)
		close_button = self.driver.\
			find_element_by_css_selector("div.minicart-wrapper a.close")
		close_button.click()

	def test_language_options(self):
		exp_options = ["ENGLISH", "FRENCH", "GERMAN"]
		act_options = []
		select_language = \
			select(self.driver.find_element_by_id("select-language"))
		self.assertEqual(2, len(select_language.options))
		for option in select_language.options:
			# get options in a list
			act_options.append(option.text)  # append() 方法:向列表的尾部添加一个新的元素。
		self.assertEqual(exp_options, act_options)

		# first_selected_option属性来检验默认/当前选择项
		self.assertEqual("ENGLISH", select_language.first_selected_option.text)

		# 选择一个语言选项，检验保存的url是否能够随着语言选项的改变而正确地变化
		select_language.select_by_visible_text("German")
		self.assertTrue("store=german" in self.driver.current_url)

		select_language = select(self.driver.find_element_by_id("select-language"))
		select_language.select_by_index(0)

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

	if __name__ == '__main__':
		unittest.main(verbosity=2)
