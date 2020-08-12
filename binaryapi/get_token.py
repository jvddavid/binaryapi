import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.chrome.options import Options


def get_token(email, senha):
    # Chrome WebDriver 85.0.4183.38
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1000x700")
    try:
        driver = webdriver.Chrome(options=chrome_options)
    except WebDriverException:
        import binaryapi.webdrivers as webdriver_files
        if os.name == 'nt':
            with open('./chromedriver.exe', 'wb') as webdriver_file:
                webdriver_file.write(webdriver_files.chrome_win32)
        elif os.name == 'posix':
            with open('./chromedriver.exe', 'wb') as webdriver_file:
                webdriver_file.write(webdriver_files.chrome_linux)
            pass
        else:
            return False
        driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://oauth.binary.com/oauth2/authorize?app_id=22259")
    driver.find_element_by_name('email').send_keys(str(email))
    driver.find_element_by_name('password').send_keys(str(senha))
    driver.find_element_by_name('login').click()
    try:
        driver.find_element_by_name('confirm_scopes').click()
    except NoSuchElementException:
        pass
    url_result = str(driver.current_url).replace('http://localhost/?', '').split('&')
    dados = {}
    for item in url_result:
        dados[str(item.split('=')[0])] = str(item.split('=')[1])
    driver.close()
    for key in dados.keys():
        if 'token' in str(key):
            return dados
    return False
