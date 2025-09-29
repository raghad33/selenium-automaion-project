from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """الصفحة الأساسية التي يرث منها جميع الصفحات"""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def find_element(self, locator):
        """إيجاد عنصر مع الانتظار"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        """النقر على عنصر مع الانتظار"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def get_title(self):
        """الحصول على عنوان الصفحة"""
        return self.driver.title

    def get_current_url(self):
        """الحصول على الرابط الحالي"""
        return self.driver.current_url