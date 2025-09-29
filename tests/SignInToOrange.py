import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.SignIn import LoginPage


class TestLogin(unittest.TestCase):
    """اختبارات تسجيل الدخول"""

    def setUp(self):
        """تهيئة قبل كل اختبار"""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.SignIn = LoginPage(self.driver)

    def tearDown(self):
        """تنظيف بعد كل اختبار"""
        self.driver.quit()

    def test_successful_login(self):
        """اختبار تسجيل دخول ناجح"""
        self.SignIn.login("Admin", "admin123")

        self.assertTrue(self.SignIn.is_login_successful())
        print("✅ تسجيل الدخول الناجح يعمل بشكل صحيح")

    def test_invalid_username(self):
        """اختبار اسم مستخدم خاطئ"""
        self.SignIn.login("WrongUser", "admin123")

        error_message = self.SignIn.get_error_message()
        self.assertIn("Invalid", error_message)
        print("✅ اكتشاف اسم المستخدم الخاطئ يعمل بشكل صحيح")

    def test_invalid_password(self):
        """اختبار كلمة مرور خاطئة"""
        self.SignIn.login("Admin", "WrongPass")

        error_message = self.SignIn.get_error_message()
        self.assertIn("Invalid", error_message)
        print("✅ اكتشاف كلمة المرور الخاطئة يعمل بشكل صحيح")


if __name__ == "__main__":
    unittest.main()