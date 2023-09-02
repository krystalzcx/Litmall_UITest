from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By

from utils.logger_util import logger
from utils.web_util import click_exception


# 商品列表页面
class GoodsListPage(BasePage):


    """商品列表页面：点击添加"""
    def click_add(self):
        # 点击“添加"按钮
        WebDriverWait(self.driver,10).until(click_exception(By.XPATH,"//*[text()='添加']"))
        # self.driver.find_element(By.XPATH,"//*[text()='添加']").click()
        #==》创建商品页面
        from page_objects.good_create_page import GoodCreatePage
        return GoodCreatePage(self.driver)

    """类目列表页面：获取操作结果"""
    def get_operate_result(self):
        # 获取冒泡消息文本
        # visibility_of_element_located 等待元素出现
        element = WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located
            ((By.XPATH, "//p[contains(text(),'创建成功')]")))
        # 消息文本
        msg = element.text
        logger.info(f'冒泡消息是:{msg}')
        # 返回消息文本
        return msg

