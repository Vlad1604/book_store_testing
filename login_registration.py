from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.get('https://practice.automationtesting.in/')
driver.maximize_window()

# 01
# my_account = driver.find_element_by_id('menu-item-50')
# my_account.click()
# user_mail = driver.find_element_by_id('reg_email')
# user_mail.send_keys('ivan@email.com')
# password = driver.find_element_by_id('password')
# password.send_keys('a%012345%S')
# register = driver.find_element_by_css_selector('input[name="register"]')
# register.click()
# driver.quit()

# 02
my_account = driver.find_element_by_id('menu-item-50')
my_account.click()
user_mail = driver.find_element_by_id('username')
user_mail.send_keys('ivan@email.com')
password = driver.find_element_by_id('password')
password.send_keys('a%012345%S')
login = driver.find_element_by_css_selector('input[value="Login"]')
login.click()
logout = driver.find_element_by_class_name('woocommerce-MyAccount-navigation-link--customer-logout')
logout_text = logout.text
assert logout_text == 'Logout'

driver.quit()
