import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import pyautogui
import pyperclip

options = webdriver.ChromeOptions()
prefs = {"profile.default_content_settings.popups": 0,            
        "download.prompt_for_download": True, 
        "download.directory_upgrade": True}
options.add_experimental_option("prefs", prefs)

url = 'https://freeditorial.com/es/books/arrivals'
autor = 'Arik Eindrok'

PATH = "C:\Program Files (x86)\Google\chromedriver.exe" 
driver = webdriver.Chrome(executable_path = PATH, options=options)

driver.get(url)

fieldsXpage = list(range(1,11))
paginas = list(range(1,6))
for page in paginas:
    for x in fieldsXpage:
        try:
                
            wait = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/article['+str(x)+']/div[1]/p[2]/a')))
            author_book = driver.find_element_by_xpath('/html/body/div[2]/article['+str(x)+']/div[1]/p[2]/a').text
            print(author_book)

            if author_book == autor:
                
                driver.find_element_by_xpath('/html/body/div[2]/article['+str(x)+']/div[1]/ul/li[1]').click() #download book link 1st step
                wait = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]')))
                
                titulo_libro = driver.find_element_by_class_name('expandbook__title').text
                
                directorio = titulo_libro
                directorio_principal = "C:/Users/andre/Downloads/Libros_freeditorial"
                path = os.path.join(directorio_principal, directorio)
                os.mkdir(path)
                wait = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[2]/ul/li[3]/a')))
                try:
                    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[2]/ul/li[3]/a').click() #download pdf    
                except Exception:
                    driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/div/ul[1]/li[2]/a').click() #download pdf                  
                
                ruta = path.replace('/','\\')
                time.sleep(5)
                
                pyperclip.copy(ruta)
                pyautogui.hotkey("ctrl", "v")       
                pyautogui.press('enter')
                time.sleep(2)
                pyautogui.press('enter')
                wait = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]')))
                
                
                driver.get('https://freeditorial.com/es/books/arrivals?page='+str(page))
                
        except Exception:
            print ('Error en registro',x, 'de la página',page)
            pass

driver.quit()
print('Programa finalizado')
