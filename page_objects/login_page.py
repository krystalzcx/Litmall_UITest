from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.logger_util import logger



class LoginPage(BasePage):
    _BASE_URL = 'https://litemall.hogwarts.ceshiren.com/#/login'

    # 元素定位变量
    __INPUT_USERNAME = (By.NAME, 'username')
    __INPUT_PASSWORD = (By.NAME, 'password')
    __BIT_LOGIN = (By.CSS_SELECTOR, '.el-button--primary')

    def login(self):
        # 访问登录页
        logger.info('登录')
        # 输入用户名
        self.do_send_keys('manage',self.__INPUT_USERNAME)
        # 输入密码
        self.do_send_keys('manage123',self.__INPUT_PASSWORD)
        # 点击登录
        self.do_find(self.__BIT_LOGIN).click()
        # 跳转到首页
        # 导入包放在这里是因为放在类上容易造成循环依赖(后续用例中会有链式调用)
        from page_objects.home_page import HomePage
        return HomePage(self.driver)
