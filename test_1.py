import time
from selenium import webdriver
from selenium.webdriver.common.by import By



def test_logging():
    driver = webdriver.Chrome() #Выбираем Google.Chrome как браузер
    driver.get('https://demo.zveno.io/ ') # Передаем в браузер ссылку и переходим по ней

    login = driver.find_element(By.CSS_SELECTOR, "[id='input-21']") #На странице ищем поле ввода логина
    login.send_keys('support@gmail.com') # Вводим в поле ввода логин

    password = driver.find_element(By.CSS_SELECTOR, "[id='input-25']") #Ищем на странице поле ввода пароля
    password.send_keys('Zz!123456') #Вводим пароль

    submit_button = driver.find_element(By.CSS_SELECTOR, "[data-type = 'c-button']") # Ищем на странице кнопку "Войти"
    submit_button.click() #Нажимаем на кнопку
    time.sleep(3) #Ждем, пока система нас авторизует

    driver.get('https://demo.zveno.io/support ') #переходим на страницу для обращения в техподдержку
    time.sleep(3) #Ожидаем открытия страницы

    Message = driver.find_element(By.CSS_SELECTOR, "[id='input-127']") #Ищем поле для ввода описания нашей проблемы
    Message.send_keys('Формирую отчет об ошибке') #Отправляем сообщение в поле для ввода

    submit_button_1 = driver.find_element(By.CSS_SELECTOR, "[name = 'Сохранить']") #Ищем на странице кнопку "Сохранить"
    submit_button_1.click() # Нажимаем на кнопку и отправляем наше сообщение





if __name__ == '__main__':
    test_logging()