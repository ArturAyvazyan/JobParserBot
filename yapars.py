import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')
driver.get('https://rabota.yandex.ru/')
driver.maximize_window()



def Beck():
    driver.back()
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, 'text').clear()
    driver.find_element(By.NAME, 'text').clear()



def find_vacancies(search_str):
    driver.find_element(By.NAME, 'text').send_keys(search_str)
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//button[@tabindex = "6"]').click()

    all_wakas = driver.find_elements(By.XPATH, '//a[@class = "link link_upped_yes serp-vacancy__name stat__click"]')
    links = [waka.get_attribute('href') for waka in all_wakas]
 

    all_flakas = driver.find_elements(By.XPATH, '//a[@class = "link serp-vacancy__name stat__click"]')
    blinks = [flaka.get_attribute('href') for flaka in all_flakas]

    all_jackass = driver.find_elements(By.TAG_NAME, ' h3')
    boka = [jackass.text for jackass in all_jackass] 
    del boka[1]


    all_salaries = driver.find_elements(By.CLASS_NAME, 'serp-vacancy__requirements')
    jinglz = [salary.text for salary in all_salaries]
        

    all_links = links + blinks
    limit = 5
    min_len = min(len(boka), len(jinglz), len(all_links), limit)
    output = ''
    for i in range(min_len):
        output += f'{i+1} вакансия: {boka[i] + jinglz[i] + all_links[i]}\n'
    
    return output[:4096]
