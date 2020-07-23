import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='C:\webdrivers\chromedriver.exe')
driver.get('https://rabota.yandex.ru/')
driver.maximize_window()

def Django():
    driver.find_element(By.NAME, 'text').send_keys('django Санкт-Петербург')
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
        

    a = ' Первая вакансия: '
    b = ' Вторая вакансия: '
    c = ' Третья вакансия: '
    d = ' Четвертая вакансия: '
    e = ' Пятая вакансия: '
    f = ' Шестая вакансия: '
    g = ' Седьмая вакансия: '
    vivod1 = a + boka[0] + jinglz[0] + blinks[0]
    vivod2 = b + boka[1] + jinglz[1] + blinks[1]
    vivod3 = c + boka[2] + jinglz[2] + blinks[2]
    vivod4 = d + boka[3] + jinglz[3] + blinks[3]
    vivod5 = e + boka[4] + jinglz[4] + blinks[4]
    vivod6 = f + boka[5] + jinglz[5] + blinks[5]
    vivod7 = g + boka[6] + jinglz[6] + blinks[6]
    return vivod1 + vivod2 + vivod3 + vivod4 + vivod5 + vivod6 + vivod7

    driver.back()
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, 'text').clear()
    driver.find_element(By.NAME, 'text').clear()

def Pyt():
    driver.find_element(By.NAME, 'text').send_keys('python Санкт-Петербург')
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//button[@tabindex = "6"]').click()
    driver.implicitly_wait(5)

    all_wakas = driver.find_elements(By.XPATH, '//a[@class = "link link_upped_yes serp-vacancy__name stat__click"]')
    links = [waka.get_attribute('href') for waka in all_wakas]
    

    all_flakas = driver.find_elements(By.XPATH, '//a[@class = "link serp-vacancy__name stat__click"]')
    blinks = [flaka.get_attribute('href') for flaka in all_flakas]
    
    all_jackass = driver.find_elements(By.TAG_NAME, ' h3')
    boka = [jackass.text for jackass in all_jackass] 
    del boka[1]


    all_salaries = driver.find_elements(By.CLASS_NAME, 'serp-vacancy__requirements')
    jinglz = [salary.text for salary in all_salaries]
        

    a = ' Первая вакансия: '
    b = ' Вторая вакансия: '
    c = ' Третья вакансия: '
    d = ' Четвертая вакансия: '
    e = ' Пятая вакансия: '
    f = ' Шестая вакансия: '
    g = ' Седьмая вакансия: '
    
    vivod1 = a + boka[0] + jinglz[0] + blinks[0]
    vivod2 = b + boka[1] + jinglz[1] + links[1]
    vivod3 = c + boka[2] + jinglz[2] + links[2]
    vivod4 = d + boka[3] + jinglz[3] + links[3]
    vivod5 = e + boka[4] + jinglz[4] + links[4]
    vivod6 = f + boka[5] + jinglz[5] + links[5]
    vivod7 = g + boka[6] + jinglz[6] + links[6]
    return vivod1 + vivod2 + vivod3 + vivod4 + vivod5 + vivod6 + vivod7

def Beck():
    driver.back()
    driver.implicitly_wait(5)
    driver.find_element(By.NAME, 'text').clear()
    driver.find_element(By.NAME, 'text').clear()
    
def PyJunior():
    driver.find_element(By.NAME, 'text').send_keys('python junior Санкт-Петербург')
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//button[@tabindex = "6"]').click()
    driver.implicitly_wait(5)

    all_wakas = driver.find_elements(By.XPATH, '//a[@class = "link link_upped_yes serp-vacancy__name stat__click"]')
    links = [waka.get_attribute('href') for waka in all_wakas]
    

    all_flakas = driver.find_elements(By.XPATH, '//a[@class = "link serp-vacancy__name stat__click"]')
    blinks = [flaka.get_attribute('href') for flaka in all_flakas]
    
    all_jackass = driver.find_elements(By.TAG_NAME, ' h3')
    boka = [jackass.text for jackass in all_jackass] 
    del boka[1]


    all_salaries = driver.find_elements(By.CLASS_NAME, 'serp-vacancy__requirements')
    jinglz = [salary.text for salary in all_salaries]
        

    a = ' Первая вакансия: '
    b = ' Вторая вакансия: '
    c = ' Третья вакансия: '
    d = ' Четвертая вакансия: '
    e = ' Пятая вакансия: '
    f = ' Шестая вакансия: '
    g = ' Седьмая вакансия: '
    
    vivod1 = a + boka[0] + jinglz[0] + blinks[0]
    vivod2 = b + boka[1] + jinglz[1] + links[1]
    vivod3 = c + boka[2] + jinglz[2] + links[2]
    vivod4 = d + boka[3] + jinglz[3] + links[3]
    vivod5 = e + boka[4] + jinglz[4] + links[4]
    return vivod1 + vivod2 + vivod3 + vivod4 + vivod5

def Web():
    driver.find_element(By.NAME, 'text').send_keys('web developer junior Санкт-Петербург')
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//button[@tabindex = "6"]').click()
    driver.implicitly_wait(5)

    all_wakas = driver.find_elements(By.XPATH, '//a[@class = "link link_upped_yes serp-vacancy__name stat__click"]')
    links = [waka.get_attribute('href') for waka in all_wakas]
    

    all_flakas = driver.find_elements(By.XPATH, '//a[@class = "link serp-vacancy__name stat__click"]')
    blinks = [flaka.get_attribute('href') for flaka in all_flakas]
    
    all_jackass = driver.find_elements(By.TAG_NAME, ' h3')
    boka = [jackass.text for jackass in all_jackass] 
    del boka[1]


    all_salaries = driver.find_elements(By.CLASS_NAME, 'serp-vacancy__requirements')
    jinglz = [salary.text for salary in all_salaries]
        

    a = ' Первая вакансия: '
    b = ' Вторая вакансия: '
    c = ' Третья вакансия: '
    d = ' Четвертая вакансия: '
    e = ' Пятая вакансия: '
    f = ' Шестая вакансия: '
    g = ' Седьмая вакансия: '
    
    vivod1 = a + boka[0] + jinglz[0] + links[0]
    vivod2 = b + boka[1] + jinglz[1] + links[1]
    vivod3 = c + boka[2] + jinglz[2] + links[2]
    vivod4 = d + boka[3] + jinglz[3] + links[3]
    vivod5 = e + boka[4] + jinglz[4] + links[4]
    vivod6 = f + boka[5] + jinglz[5] + links[5]
    vivod7 = g + boka[6] + jinglz[6] + links[6]
    return vivod1 + vivod2 + vivod3 + vivod4 + vivod5 + vivod6 + vivod7

def Selo():
    driver.find_element(By.NAME, 'text').send_keys('selenium Санкт-Петербург')
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//button[@tabindex = "6"]').click()
    driver.implicitly_wait(5)

    all_wakas = driver.find_elements(By.XPATH, '//a[@class = "link link_upped_yes serp-vacancy__name stat__click"]')
    links = [waka.get_attribute('href') for waka in all_wakas]
    

    all_flakas = driver.find_elements(By.XPATH, '//a[@class = "link serp-vacancy__name stat__click"]')
    blinks = [flaka.get_attribute('href') for flaka in all_flakas]
    
    all_jackass = driver.find_elements(By.TAG_NAME, ' h3')
    boka = [jackass.text for jackass in all_jackass] 
    del boka[1]


    all_salaries = driver.find_elements(By.CLASS_NAME, 'serp-vacancy__requirements')
    jinglz = [salary.text for salary in all_salaries]
        

    a = ' Первая вакансия: '
    b = ' Вторая вакансия: '
    c = ' Третья вакансия: '
    d = ' Четвертая вакансия: '
    e = ' Пятая вакансия: '
    f = ' Шестая вакансия: '
    g = ' Седьмая вакансия: '
    
    vivod1 = a + boka[0] + jinglz[0] + blinks[0]
    vivod2 = b + boka[1] + jinglz[1] + links[1]
    vivod3 = c + boka[2] + jinglz[2] + links[2]
    vivod4 = d + boka[3] + jinglz[3] + links[3]
    vivod5 = e + boka[4] + jinglz[4] + links[4]
    vivod6 = f + boka[5] + jinglz[5] + links[5]
    vivod7 = g + boka[6] + jinglz[6] + links[6]
    return vivod1 + vivod2 + vivod3 + vivod4 + vivod5 + vivod6 + vivod7
