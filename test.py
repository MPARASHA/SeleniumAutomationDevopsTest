# Import Module
import os
import pathlib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

os.environ['PATH'] += r"."

options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")

prefs = {"profile.default_content_settings.popups": 0,
            "download.default_directory": 
                        str(pathlib.Path().resolve()) + r"\downloads",
            "directory_upgrade": True}

options.add_experimental_option("prefs", prefs)


driver = webdriver.Chrome(options= options)

  
# Open URL
driver.get(
    'http://demo.automationtesting.in/FileDownload.html')
  
# Enter text
driver.find_element(By.ID, 'textbox').send_keys("Hello world")
  
# Generate Text File
driver.find_element(By.ID,'createTxt').click()
  
# Click on Download Button
driver.find_element(By.ID,'link-to-download').click()