from selenium import webdriver

# browser exposes an executable file
# through Selenium test we need to invoke the executable file which will then invoke actual browser
driver = webdriver.Chrome(executable_path='C:\\Webdrivers\\Chromedriver92\\chromedriver.exe')

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
print(driver.current_url)




driver.close()