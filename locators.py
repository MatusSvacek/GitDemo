from selenium import webdriver

# browser exposes an executable file
# through Selenium test we need to invoke the executable file which will then invoke actual browser
driver = webdriver.Chrome(executable_path='C:\\Webdrivers\\Chromedriver92\\chromedriver.exe')
driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_css_selector("input[name='name']").send_keys("Matus")
driver.find_element_by_name("email").send_keys("email")


driver.find_element_by_id("exampleCheck1").click()