import pytest
from selenium import webdriver
from PageObjects.LoginPage import Login
import time

class Test_001_Login:
    base_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"

    def test_login_page_title(self):
        driver = webdriver.Chrome()
        driver.get(self.base_url)
        assert "OrangeHRM" in driver.title
        driver.quit()

    def test_login_valid(self):
        driver = webdriver.Chrome()
        driver.get(self.base_url)

        login = Login(driver)
        login.setUsername(self.username)
        login.setPassword(self.password)
        login.clickLogin()
        time.sleep(3)

        assert "dashboard" in driver.current_url.lower()
        driver.quit()

    def test_leave_menu_clickable(self):
        driver = webdriver.Chrome()
        driver.get(self.base_url)

        login = Login(driver)
        login.setUsername(self.username)
        login.setPassword(self.password)
        login.clickLogin()

        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        leave_menu_xpath = "//span[text()='Leave']"

        # Click the Leave menu
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, leave_menu_xpath))
        ).click()

        # Wait until URL contains "/leave"
        WebDriverWait(driver, 10).until(
            EC.url_contains("leave")
        )

        # Just check that page loaded correctly
        assert "leave" in driver.current_url.lower()

        driver.quit()


    def test_logout(self):
        driver = webdriver.Chrome()
        driver.get(self.base_url)

        login = Login(driver)
        login.setUsername(self.username)
        login.setPassword(self.password)
        login.clickLogin()

        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        profile_icon_xpath = "//span[@class='oxd-userdropdown-tab']"
        logout_link_xpath = "//a[text()='Logout']"

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, profile_icon_xpath))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, logout_link_xpath))
        ).click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h5[text()='Login']"))
        )

        assert "login" in driver.current_url.lower()
        driver.quit()
    