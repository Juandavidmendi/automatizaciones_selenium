import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class MercadoLibre(unittest.TestCase):

	def setUp(self):
		self.driver = webdriver.Chrome(executable_path=r'C:\dchrome\chromedriver.exe')
		driver = self.driver
		driver.get("http://mercadoLibre.com")
		driver.maximize_window()

	def test_search_ps4(self):
		driver = self.driver

		country = driver.find_element_by_id('CO')
		country.click()

		search_field = driver.find_element_by_name('as_word')
		search_field.click()
		search_field.clear()
		search_field.send_keys('playstation 4')
		search_field.submit()
		sleep(3)

		location = driver.find_element_by_partial_link_text('Bogotá D.C.')
		location.send_keys(Keys.ENTER)
		sleep(3)

		condition = driver.find_element_by_partial_link_text('Nuevo')
		condition.send_keys(Keys.ENTER)
		sleep(3)

		order_menu = driver.find_element_by_class_name('andes-dropdown__trigger')
		order_menu.send_keys(Keys.RETURN)
		sleep(3)

		higher_price =driver.find_element_by_css_selector('#root-app > div > div > section > div.ui-search-view-options__container > div > div > div > div.ui-search-sort-filter > div > div > div > ul > li:nth-child(3) > a > div > div')
		higher_price.click()
		sleep(3)

		articles = []
		prices = []

		for i in range(5):
			article_name = driver.find_element_by_css_selector(f'#root-app > div > div > section > ol > li:nth-child({i + 1})').text 
			articles.append(article_name)

			article_price = driver.find_element_by_css_selector(f'#root-app > div > div > section > ol > li:nth-child({i + 1}) > div > div > div.ui-search-result_content-wrapper > div.ui-search-resultcontent-columns > div.ui-search-resultcontent-column.ui-search-resultcontent-column--left > div.ui-search-itemgroup.ui-search-itemgroup--price > a > div > div > span.price-tag.ui-search-price_part > span.price-tag-amount > span.price-tag-fraction').text
			prices.append(article_price)

		print(articles, prices)
		sleep(3)

	def tearDown(self):
		self.driver.close()

if __name__ == '__main__':
	unittest.main(verbosity = 2)