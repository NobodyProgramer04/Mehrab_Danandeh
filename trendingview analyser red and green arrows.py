from selenium import webdriver
from selenium.webdriver.common.by import By
from plyer import notification
import time

# تنظیمات پیامک
def send_notification(message):
    notification.notify(
        title='عنوان نوتیفیکیشن',
        message=message,
        app_name='نام برنامه',
        timeout=5
    )

# تنظیمات درایور و سایت TradingView
driver_path = '/path/to/chromedriver'
url = 'https://www.tradingview.com/'

# راه‌اندازی درایور
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('executable_path=' + driver_path)
driver = webdriver.Chrome(options=options)

# ورود به صفحه TradingView و کلیک بر روی ایندیکیتور Intraday Volume Swings
driver.get(url)
driver.implicitly_wait(10)
indicator_xpath = "//*[contains(text(), 'Intraday Volume Swings')]"
indicator = driver.find_element(By.XPATH, indicator_xpath)
indicator.click()

# پیدا کردن فلش های سبز و قرمز و ارسال پیامک
counter = 0 # تعداد دفعات اجرای حلقه
while True:
    arrow_css_selector = ".tvchart-intraday-volume-swing__arrow"
    arrows = driver.find_elements(By.CSS_SELECTOR, arrow_css_selector)
    for arrow in arrows:
        arrow_class = arrow.get_attribute("class")
        if "up" in arrow_class:
            send_notification("Green arrow detected!")
        elif "down" in arrow_class:
            send_notification("Red arrow detected!")
    if counter == 10: # تعداد دفعات اجرای حلقه
        break
    counter += 1
    time.sleep(5) # تاخیر بین هر بار اجرا کردن حلقه

# بستن درایور
driver.quit()