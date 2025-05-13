from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get('https://practice.automationtesting.in/')
driver.implicitly_wait(5)
driver.maximize_window()

my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
user_mail = driver.find_element_by_id('username')
user_mail.send_keys('ivan@email.com')
password = driver.find_element_by_id('password')
password.send_keys('a%012345%S')
remember = driver.find_element_by_id('rememberme')
remember.click()
login = driver.find_element_by_css_selector('input[value="Login"]')
login.click()
shop = driver.find_element_by_id('menu-item-40')
shop.click()  # часто здесь застревает, пишет устаревший элемент не найден

# 01
# html5_forms = driver.find_element_by_css_selector('img[alt="Mastering HTML5 Forms"]')
# html5_forms.click()
# title_html5 = driver.find_element_by_css_selector('div>h1[itemprop="name"]')
# title_html5_text = title_html5.text
# assert title_html5_text == 'HTML5 Forms'
# driver.quit()

# 02
# category_html = driver.find_element_by_css_selector('.cat-item-19>a')
# category_html.click()
# count_product = driver.find_elements_by_class_name('product_cat-html')
# if len(count_product) == 3:
#     print("В категории 3 товара")
# else:
#     print("Количество товаров в категории: " + str(len(count_product)))
#   # если не нужен print: assert len(count_product) == 3
# driver.quit()

# 03
# sort = driver.find_element_by_css_selector("[value='menu_order']")
# sort_def = driver.find_element_by_css_selector("[selected='selected']")
# if sort == sort_def:
#     print('Выбран вариант сортировки по умолчанию')
# else:
#     print('Выбрана другая сортировка')
# cat_prod = driver.find_element_by_class_name('orderby')
# select = Select(cat_prod)
# select.select_by_visible_text('Sort by price: high to low')
# cat_prod = driver.find_element_by_class_name('orderby')
# select = Select(cat_prod)
# select.select_by_value('menu_order')  # не понятно, п.6 должен вернуть назад к сортировке по умолчанию?
#             # тоже не понятнор: здесь опять выполнить от большей к меньшей и провести тест?
# cat_prod = driver.find_element_by_class_name('orderby')
# select = Select(cat_prod)
# select.select_by_visible_text('Sort by price: high to low')
# price_desc = driver.find_element_by_css_selector('select>[value="price-desc"]')
# sort_def = driver.find_element_by_css_selector("[selected='selected']")
# if price_desc == sort_def:
#     print('Выбран вариант сортировки от большей к меньшей')
# else:
#     print('Выбран другой вариант сортировки')
# driver.quit()

# 04
# android_quick_start = driver.find_element_by_css_selector('img[alt="Android Quick Start Guide"]')
# android_quick_start.click()
# old_price = driver.find_element_by_css_selector('.price>del>span')
# old_price_text = old_price.text
# new_price = driver.find_element_by_css_selector('.price>ins>span')
# new_price_text = new_price.text
# assert old_price_text == '₹600.00'
# assert new_price_text == '₹450.00'
# book_open = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, '.wp-post-image'))
# )
# book_open.click()
# book_close = WebDriverWait(driver, 10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, '.pp_close'))
# )
# book_close.click()
# driver.quit()

# 05


driver.quit()
