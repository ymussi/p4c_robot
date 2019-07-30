from selenium import webdriver
from random import randint
from selenium.webdriver.common.keys import Keys
from time import sleep
from configparser import ConfigParser

config = ConfigParser()
config.read('../config/config.ini')

url = config['SITES']['URL']

def gerar_cads():
    names = ['Joao Andrinho', 'Andra Carlos', 'Carlos Andrews']
    emails = ['teste@teste.com', 'zedascoves@teste.com.br', 'testedoandrews@andrin.com']
    senhas = ['123mUdar.', 'tesTe132.', 'Andrin0!']
    idx_name = randint(0, (len(names) - 1))
    idx_mail = randint(0, (len(emails) - 1))
    idx_passwd = randint(0, (len(senhas) - 1))
    nome = names[idx_name]
    passwd = senhas[idx_passwd]
    email = emails[idx_mail]

    return nome, passwd, email

def robot_maroto():
    driver = webdriver.Chrome(executable_path=r"../utils/chromedriver_mac")
    
    driver.get(url)
    driver.maximize_window()

    btn_sign = driver.find_element_by_class_name('c-btn')
    btn_sign.click()

    full_name = driver.find_element_by_class_name('c-input')
    full_name.send_keys(gerar_cads()[0])

    user = driver.find_element_by_name('username')
    user.send_keys(gerar_cads()[0].lower().replace(" ", ""))

    email = driver.find_element_by_name('email')
    email.send_keys(gerar_cads()[2].lower().replace(" ", ""))

    senha = gerar_cads()[1]
    passwd = driver.find_element_by_name('password')
    passwd.send_keys(senha)

    passwd2 = driver.find_element_by_name('password2')
    passwd2.send_keys(senha)

    check = driver.find_element_by_name('terms')
    check.click()

    sign_in = driver.find_element_by_name('signup_acc')
    sign_in.click()

    sleep(10)

if __name__ == "__main__":
    robot_maroto()
    pass