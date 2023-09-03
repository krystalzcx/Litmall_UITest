import allure
from selenium import webdriver
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


# 父类
# todo:很多页面能使用到的功能就可以考虑封装到base_page里
class BasePage:
    _BASE_URL = ''

    def __init__(self,base_driver = None):
        # todo:什么时候传递base_driver？
        if base_driver:
            self.driver = base_driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(3)
            self.driver.maximize_window()

        if not self.driver.current_url.startswith("http"):
            self.driver.get(self._BASE_URL)
            print('运行到此')


    def do_find(self, by, locator=None):
        '''获取单个元素'''
        if locator:
            return self.driver.find_element(by,locator)
        else:
            # 如果传递的是元组或者其他复合对象，那么就进行解包
            return self.driver.find_element(*by)

    def do_finds(self, by, locator=None):
        '''获取多个元素'''
        if locator:
            return self.driver.find_elements(by,locator)
        else:
            # 如果传递的是元组或者其他复合对象，那么就进行解包
            return self.driver.find_elements(*by)

    # 为登录操作封装的
    def do_send_keys(self, value, by, locator=None):
        ele = self.do_find(by,locator)
        ele.clear()
        ele.send_keys(value)

    # 退出浏览器
    def do_quit(self):
        self.driver.quit()


    def get_screen(self):
        timestamp = int(time.time())
        # 注意：一定提前创建好image路径
        image_path = f'./image/image_{timestamp}.PNG'
        # 截图
        self.driver.save_screenshot(image_path)
        # 将截图放到报告的数据中
        allure.attach.file(image_path,name='picture',
                           attachment_type=allure.attachment_type.PNG)


    # 等待元素出现
    def wait_element_until_visible(self,locator:tuple):
        # visibility_of_element_located 等待元素出现
        return  (WebDriverWait(self.driver,10)\
                 .until(expected_conditions.visibility_of_element_located(locator)))
