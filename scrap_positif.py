import random
from selenium.webdriver.common.by import By
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
 
#lambdatest setup and opening the desired website
username = "--"
accessToken = "--"
gridUrl = "hub.lambdatest.com/wd/hub"
 
capabilities = {
    'LT:Options' : {
        "user" : "--",
        "accessKey" : "--",
        "build" : "Test",
        "name" : "Test",
        "platformName" : "Windows 11",
    },
    "browserName" : "Chrome",
    "browserVersion" : "103.0",
}
 
 
url = "https://"+username+":"+accessToken+"@"+gridUrl
 
browser = webdriver.Remote(
    command_executor=url,
    desired_capabilities=capabilities
)
 
browser.maximize_window()
browser.get("http://51.79.230.10:4200/soal-tes-qa/public/")
 

level = browser.find_element(By.ID, "beginner")
level.click()

first_name = browser.find_element(By.NAME, "nama")
first_name.send_keys("Nurchulis")
 
last_name = browser.find_element(By.NAME, "tempat_lahir")
last_name.send_keys("Bantul")
 
random_email = str(random.randint(0,99999)) + "@gmail.com"
 
email = browser.find_element(By.NAME, "email")
email.send_keys(random_email)
 
telephone = browser.find_element(By.NAME, "notelp")
telephone.send_keys("+351999888777")
 
alamat = browser.find_element(By.NAME, "alamat")
alamat.send_keys("bantul")
 
tanggal_lahir = browser.find_element(By.NAME, "tanggal_lahir")
tanggal_lahir.send_keys("31/07/1998")

file_image = browser.find_element(By.NAME, "image")
file_image.send_keys(os.path.join(os.getcwd(), 'images.png'))


file_image_ktp = browser.find_element(By.NAME, "ktp")
file_image_ktp.send_keys(os.path.join(os.getcwd(), 'images.png'))

submit_btn = browser.find_element(By.ID, "submitForm")
submit_btn.submit()

print("DONE")

browser.quit()