from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.logger_util import logger



class LoginPage(BasePage):
    _BASE_URL = 'https://litemall.hogwarts.ceshiren.com/#/login'
    def login(self):
        logger.info('登录')
        # 这步打开初始登录页面，父类BasePage已经实现，会自动执行父类初始化方法
        # self.driver.get(_BASE_URL)
        self.driver.find_element(By.NAME, 'username').clear()
        self.driver.find_element(By.NAME, 'password').clear()
        # 输入账号密码
        self.driver.find_element(By.NAME, 'username').send_keys('manage')
        self.driver.find_element(By.NAME, 'password').send_keys('manage123')
        # 点击登录
        self.driver.find_element(By.CSS_SELECTOR, '.el-button--primary').click()
        # 跳转到首页
        # 导入包放在这里是因为放在类上容易造成循环依赖(后续用例中会有链式调用)
        from page_objects.home_page import HomePage
        return HomePage(self.driver)
