import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions
from seleniumMinder import debugpref
from random import randint
symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '!', '!', '1']
symbolsname = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]
driver = webdriver.Chrome()
getAttr = input('Использовать debug? Y/n')
url = 'https://www.roblox.com/'
url1 = 'https://www.riotgames.com/'
print(f'Доступные платформы: Roblox, Valorant')
getGen = input('Генерировать аккаунты какой платформы(?): ')
def roblox():
    month = '//*[@id="MonthDropdown"]'
    day = '//*[@id="DayDropdown"]'
    year = '//*[@id="YearDropdown"]'
    name = '//*[@id="signup-username"]'
    password = '//*[@id="signup-password"]'
    malebutton = '//*[@id="MaleButton"]'
    femalebutton = '//*[@id="FemaleButton"]'
    signupbutton = '//*[@id="signup-button"]'
    robloxaccs = open('robloxaccs', 'w')
    if getAttr.lower() == 'y': print(f'{debugpref}запуск общего цикла. Для остановки завершите программу.')
    while True:
        driver.get(url)
        monthb = driver.find_element(By.XPATH, month)
        dayb = driver.find_element(By.XPATH, day)
        yearb = driver.find_element(By.XPATH, year)
        nameb = driver.find_element(By.XPATH, name)
        passwordb = driver.find_element(By.XPATH, password)
        malebuttonb = driver.find_element(By.XPATH, malebutton)
        femalebuttonb = driver.find_element(By.XPATH, femalebutton)
        signupbuttonb = driver.find_element(By.XPATH, signupbutton)
        monthb.click()
        mon = driver.find_element(By.XPATH, '//*[@id="MonthDropdown"]/option[3]')
        mon.click()
        dayb.click()
        d = driver.find_element(By.XPATH, '/html/body/div[3]/div/section/div/div[2]/div[1]/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div[2]/select/option[9]')
        d.click()
        yearb.click()
        y = driver.find_element(By.XPATH, '//*[@id="YearDropdown"]/option[25]')
        y.click()
        newpass = ''
        for i in range(10):newpass += symbols[randint(0, len(symbols)-1)]
        passwordb.send_keys(newpass)
        newname = ''
        for i in range(7): newname += symbolsname[randint(0, len(symbolsname)-1)]
        nameb.send_keys(newname)
        if randint(0,1) == 0:femalebuttonb.click()
        else: malebuttonb.click()
        signupbuttonb.click()
        robloxaccs.write(f'{newname}:{newpass}\n')
        if getAttr.lower() == 'y': print(f'{debugpref}аккаунт записан в файл.')
        time.sleep(3)
def valorant():
    time.sleep(0)
    #Копировать из домашнего файла
if getGen.lower() == 'roblox':
    print('Генерирование аккаунтов Roblox...')
    print('Каптча присутствует, прокси не используется.')
    driver.get(url)
    try:
        roblox()
    except Exception as error:
        if error == 'Message: element click intercepted: Element <button id="signup-button" type="button" class="btn-primary-md signup-submit-button btn-full-width" name="signupSubmit" disabled="">...</button> is not clickable at point (509, 640). Other element would receive the click: <div class="terms-agreement">...</div>':
            roblox()
        else:
            print(error)
elif getGen.lower() == 'valorant':
    print('Генерирование аккаунтов Riot Games..')
    print('Каптча присутствует, прокси используется(Турция).')
    driver.get(url1)
    try:
        valorant()
    except Exception as error:
        print(error)



