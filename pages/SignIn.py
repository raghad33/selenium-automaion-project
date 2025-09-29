import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .BaseTest import BasePage


class LoginPage(BasePage):
    """Page Object Model for login functionality"""

    # Locators - جميع محددات العناصر في مكان واحد
    USERNAME_FIELD = (By.NAME, "username")
    PASSWORD_FIELD = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    ERROR_MESSAGE = (By.CLASS_NAME, "oxd-alert-content-text")
    DASHBOARD_HEADER = (By.CLASS_NAME, "oxd-topbar-header-breadcrumb")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://opensource-demo.orangehrmlive.com/"

    def open_login_page(self):
        """فتح صفحة التسجيل"""
        self.driver.get(self.url)
        return self

    def enter_username(self, username):
        """إدخال اسم المستخدم"""
        self.driver.find_element(*self.USERNAME_FIELD).clear()
        self.driver.find_element(*self.USERNAME_FIELD).send_keys(username)
        time.sleep(2)
        return self  # للـ method chaining

    def enter_password(self, password):
        """إدخال كلمة المرور"""
        self.driver.find_element(*self.PASSWORD_FIELD).clear()
        self.driver.find_element(*self.PASSWORD_FIELD).send_keys(password)
        time.sleep(2)
        return self

    def click_login(self):
        """النقر على زر التسجيل"""
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self

    def login(self, username="Admin", password="admin123"):
        """تسجيل الدخول الكامل"""
        self.open_login_page()
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    def is_login_successful(self):
        """التحقق من نجاح التسجيل"""
        try:
            self.wait.until(EC.presence_of_element_located(self.DASHBOARD_HEADER))
            return True
        except:
            return False

    def get_error_message(self):
        """الحصول على رسالة الخطأ إذا فشل التسجيل"""
        try:
            return self.driver.find_element(*self.ERROR_MESSAGE).text
        except:
            return "No error message found"

    def wait_for_page_load(self):
        """انتظار تحميل صفحة التسجيل"""
        self.wait.until(EC.presence_of_element_located(self.USERNAME_FIELD))
        return self