from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    username_input_xpath = "//input[@placeholder='Username']"
    password_input_xpath = "//input[@placeholder='Password']"
    login_button_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.username_input_xpath))
        ).send_keys(username)

    def setPassword(self, password):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.password_input_xpath))
        ).send_keys(password)

    def clickLogin(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button_xpath))
        ).click()
