import time
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get('https://practice.automationtesting.in/')
driver.implicitly_wait(5)
driver.maximize_window()

# 01
# my_account = driver.find_element_by_id('menu-item-50')
# my_account.click()
# user_mail = driver.find_element_by_id('username')
# user_mail.send_keys('ivan@email.com')
# password = driver.find_element_by_id('password')
# password.send_keys('a%012345%S')
# remember = driver.find_element_by_id('rememberme')
# remember.click()
# login = driver.find_element_by_css_selector('input[value="Login"]')
# login.click()
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()  # часто здесь застревает, пишет устаревший элемент не найден
# html5_forms = driver.find_element_by_css_selector('img[alt="Mastering HTML5 Forms"]')
# html5_forms.click()
# title_html5 = driver.find_element_by_css_selector('div>h1[itemprop="name"]')
# title_html5_text = title_html5.text
# assert title_html5_text == 'HTML5 Forms'
# driver.quit()

# 02
# my_account = driver.find_element_by_id('menu-item-50')
# my_account.click()
# user_mail = driver.find_element_by_id('username')
# user_mail.send_keys('ivan@email.com')
# password = driver.find_element_by_id('password')
# password.send_keys('a%012345%S')
# remember = driver.find_element_by_id('rememberme')
# remember.click()
# login = driver.find_element_by_css_selector('input[value="Login"]')
# login.click()
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()  # часто здесь застревает, пишет устаревший элемент не найден
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
# my_account = driver.find_element_by_id('menu-item-50')
# my_account.click()
# user_mail = driver.find_element_by_id('username')
# user_mail.send_keys('ivan@email.com')
# password = driver.find_element_by_id('password')
# password.send_keys('a%012345%S')
# remember = driver.find_element_by_id('rememberme')
# remember.click()
# login = driver.find_element_by_css_selector('input[value="Login"]')
# login.click()
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()  # часто здесь застревает, пишет устаревший элемент не найден
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
# my_account = driver.find_element_by_id('menu-item-50')
# my_account.click()
# user_mail = driver.find_element_by_id('username')
# user_mail.send_keys('ivan@email.com')
# password = driver.find_element_by_id('password')
# password.send_keys('a%012345%S')
# remember = driver.find_element_by_id('rememberme')
# remember.click()
# login = driver.find_element_by_css_selector('input[value="Login"]')
# login.click()
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()  # часто здесь застревает, пишет устаревший элемент не найден
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
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# html5_webapp = driver.find_element_by_css_selector(".post-182 [rel='nofollow']")
# html5_webapp.click()
# basket = driver.find_element_by_css_selector('.wpmenucart-contents')
# basket.click()
# count_item = driver.find_element_by_css_selector('.wpmenucart-contents>.cartcontents')
# count_item_text = count_item.text
# price = driver.find_element_by_css_selector('a>.amount')
# price_text = price.text
# assert count_item_text == '1 Item'
# assert price_text == '₹180.00'
# view_basket = driver.find_element_by_css_selector('.wpmenucart-contents')
# view_basket.click()
# subtotal = WebDriverWait(driver, 10).until(
#      EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.cart-subtotal .amount'), '₹180.00')
# )
# total = WebDriverWait(driver, 10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.order-total .amount'), '₹183.60')
# )
# driver.quit()

# 06
# shop = driver.find_element_by_id('menu-item-40')
# shop.click()
# driver.execute_script('window.scrollBy(0, 300);')
# html5_webapp = driver.find_element_by_css_selector(".post-182 [rel='nofollow']")
# html5_webapp.click()
# time.sleep(3)
# js_data = driver.find_element_by_css_selector(".post-180 [rel='nofollow']")
# js_data.click()
# basket = driver.find_element_by_css_selector('.wpmenucart-contents')
# basket.click()
# time.sleep(5)
# remove = driver.find_element_by_css_selector('.cart_item .remove')
# remove.click()
# time.sleep(7)
# undo = driver.find_element_by_css_selector('.woocommerce-message a')
# undo.click()
# quantity = driver.find_element_by_css_selector('.product-quantity input')
# quantity.clear()
# quantity.send_keys(3)
# update = driver.find_element_by_css_selector("[value='Update Basket']")
# update.click()
# quantity = driver.find_element_by_css_selector('.product-quantity input')
# quantity_value = quantity.get_attribute('value')
# assert quantity_value == '3'
# time.sleep(3)
# coupon = driver.find_element_by_css_selector('[value="Apply Coupon"]')
# coupon.click()
# message = driver.find_element_by_css_selector('.woocommerce-error')
# message_text = message.text
# assert message_text == 'Please enter a coupon code.'
# driver.quit()

# 07
shop = driver.find_element_by_id('menu-item-40')
shop.click()
driver.execute_script('window.scrollBy(0, 300);')
html5_webapp = driver.find_element_by_css_selector(".post-182 [rel='nofollow']")
html5_webapp.click()
time.sleep(3)
basket = driver.find_element_by_css_selector('.wpmenucart-contents')
basket.click()
time.sleep(5)
process = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '.wc-proceed-to-checkout a'))
)
process.click()
first_name = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'billing_first_name'))
)
first_name.send_keys('Ivan')
last_name = driver.find_element_by_id('billing_last_name')
last_name.send_keys('Orlov')
email = driver.find_element_by_id('billing_email')
email.send_keys('IO@email.com')
phone = driver.find_element_by_id('billing_phone')
phone.send_keys('1023456789')
country = driver.find_element_by_css_selector('#s2id_billing_country [role="presentation"]')
country.click()
country_text = driver.find_element_by_id('s2id_autogen1_search')
country_text.send_keys('Russia')
country_rus = driver.find_element_by_class_name('select2-match')
country_rus.click()
address_street = driver.find_element_by_id('billing_address_1')
address_street.send_keys('Почтовая')
address_city = driver.find_element_by_css_selector('input#billing_city')
address_city.send_keys('Орёл')
address_state = driver.find_element_by_css_selector('input#billing_state')
address_state.send_keys('Орловская обл.')
postcode = driver.find_element_by_css_selector('input#billing_postcode')
postcode.send_keys('123456')
driver.execute_script('window.scrollBy(0, 600);')
time.sleep(5)
pay = driver.find_element_by_id('payment_method_cheque')
pay.click()
place_order = driver.find_element_by_id('place_order')
place_order.click()
message = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '.woocommerce-thankyou-order-received'),
    'Thank you. Your order has been received.')
)
message_pay = WebDriverWait(driver, 10).until(
    EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-35"]/div/div[1]/table/tfoot/tr[3]/td'),
    'Check Payments')
)
driver.quit()