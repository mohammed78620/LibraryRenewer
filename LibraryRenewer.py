from selenium import webdriver

#open chrome browser
browser = webdriver.Chrome("C:/WebDriver/chromedriver.exe")
browser.get('http://library.city.ac.uk/patroninfo')

#input keys into username box
username_input = browser.find_element_by_id("extpatid")
username_input.send_keys("insert username")

#input keys into password box
password_input = browser.find_element_by_id("extpatpw")
password_input.send_keys("insert password")

#press login button
login_button = browser.find_element_by_id("submit")
login_button.click()

#click renew button
renew_button = browser.find_element_by_css_selector("#checkout_form > a:nth-child(9) > div")
renew_button.click()

#click confirm renewal button
confirm_renew_button = browser.find_element_by_css_selector("#checkoutbuttons1 > a:nth-child(1) > div")
confirm_renew_button.click()

browser.quit()
