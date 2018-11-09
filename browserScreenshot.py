from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#Driver is the chrome instance
DRIVER = input("Path to Web Driver?")
username = input("Google Account Username?")
password = input("Google Account Password?")
url = input("URL of your book?")
#Driver for me: C:\Data\Programs\chromedriver_win32\chromedriver.exe
driver = webdriver.Chrome(DRIVER)

#Going to the login page.
driver.get('https://accounts.google.com/signin/v2/identifier?hl=EN&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
action = webdriver.ActionChains(driver)

#Finding the email form and clicking next
emailElem = driver.find_element_by_xpath('//*[@id="identifierId"]')

######## GOOGLE ACCOUNT USERNAME || TYPE IN BETWEEN QUOTES ########
emailElem.send_keys(username)
driver.find_element_by_xpath('//*[@id="identifierNext"]').click()

#Letting the next page load
time.sleep(1)

#Getting the password form, filling it in and clicking next.
passwordElem = driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
######### GOOGLE ACCOUNT PASSWORD || TYPE IN BETWEEN QUOTES ########
passwordElem.send_keys(password)
driver.find_element_by_xpath('//*[@id="passwordNext"]').click()

#Let the page load
time.sleep(1)
#Go to the next webpage
#Test Book: https://play.google.com/books/reader?id=iqY-DwAAQBAJ&printsec=frontcover&pg=GBS.PP1
driver.get(url)

#Go to the first iframe and switch the browswer to focus on it and its own HTML
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))

#Path to the text that says the number of pages its got
tpXpath = "/html/body/div[3]/div[2]/table[1]/tbody/tr/td[2]/div/span"

totalPages_obj = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, tpXpath)))
totalPages = int(totalPages_obj.text[2:])

#The xpath of the next button
xpath = "/html/body/div[3]/div[2]/table[1]/tbody/tr/td[3]/div/div[2]"

#Get the total times the program should loop, knowing the total pages.
totalPages = int(totalPages/2 + 4)

#Go through all the pages, take screenshots and find the 'next page button' and click it. Loop that.
for pageNum in range(totalPages):
    screenshot = driver.save_screenshot("C:/Data/Programming Projects/bookScraper/example prints/page" + str(pageNum+1) + ".png")
    button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
    button.click()

#Close the session
driver.quit()

#TODO: Take pictures of all the images and put them into a pdf
