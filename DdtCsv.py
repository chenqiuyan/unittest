import csv
import unittest
from ddt import ddt, data, unpack
from selenium import webdriver


def get_data(file_name):
	# create an empty list to store rows
	rows = []
	# open the csv file
	data_file = open(file_name, "rb")
	# create a csv reader from csv file
	reader = csv.reader(data_file)
	# skip the headers
	next(reader, None)
	# add rows from reader to list
	for row in reader:
		rows.append(row)
	return rows
@ddt
class SearchCsvDDT(unittest.TestCase):
	def setUp(self):
		self.driver = webdriver.Chrome()
		self.driver.implicitly_wait(30)
		self.driver.maximize_window()

		self.driver.get("https://baidu.com/")

	# get the data from specified cav file by calling the get_data function
	@data(*get_data("testdata.csv"))
	@unpack
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
