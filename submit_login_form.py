from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

from time import sleep

#if you want to use a headless mode.
#options = Options()
#options.headless = True
#driver = webdriver.Firefox(options=options)
driver = webdriver.Firefox()

url = 'https://shopping-najmi.herokuapp.com/login/'

username1 = "imad@gmail.com"
password1 = "123456"

#The driver.get method will navigate to a page given by the URL
driver.get(url)

#WebDriver offers a number of ways to find elements using one of the find_element_by_* methods
username = driver.find_element_by_name('email')
password = driver.find_element_by_name('password')
btn = driver.find_element_by_css_selector('button[type="submit"]')

# to clean inputs from default values
username.clear()
password.clear()

# fill inputs by given data
username.send_keys(username1)
password.send_keys(password1)

#submit the form
btn.click()

#close the driver
driver.close()
	