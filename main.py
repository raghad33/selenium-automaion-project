from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.SignIn import LoginPage
import time


def main():
    """الدالة الرئيسية لتشغيل التسجيل"""
    try:
        # تهيئة المتصفح
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # إنشاء كائن صفحة التسجيل
        SignIn = LoginPage(driver)

        # تنفيذ التسجيل
        print("🚀 بدء عملية التسجيل...")
        driver.implicitly_wait(10)
        SignIn.login()

        # التحقق من النتيجة
        if SignIn.is_login_successful():
            print("✅ تم التسجيل بنجاح!")
            print(f"📄 العنوان: {SignIn.get_title()}")
            print(f"🔗 الرابط: {SignIn.get_current_url()}")
        else:
            print("❌ فشل التسجيل")
            print(f"📝 رسالة الخطأ: {SignIn.get_error_message()}")

        # انتظار لعرض النتيجة
        time.sleep(3)

    except Exception as e:
        print(f"💥 حدث خطأ: {e}")

    finally:
        # إغلاق المتصفح
        if 'driver' in locals():
            driver.quit()
            print("🔒 تم إغلاق المتصفح")


if __name__ == "__main__":
    main()