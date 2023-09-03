from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
from utils.web_util import click_exception
import logging

# 商品列表页面
class GoodsListPage(BasePage):

    __BIT_ADD = (By.XPATH,"//*[text()='添加']")
    __MSG_ADD_OPERATE = (By.XPATH, "//p[contains(text(),'创建成功')]")
    __MSG_DELETE_OPERATE = (By.XPATH, "//p[contains(text(),'删除')]")



    """商品列表页面：点击添加"""
    def click_add(self):
        logging.info('商品列表：点添加')
        # 点击“添加"按钮
        self.do_find(self.__BIT_ADD).click()
        #==》创建商品页面
        from page_objects.good_create_page import GoodCreatePage
        return GoodCreatePage(self.driver)

    """类目列表页面：获取操作结果"""
    def get_operate_result(self):
        # 获取冒泡消息文本
        element =self.wait_element_until_visible(self.__MSG_ADD_OPERATE)
        # 消息文本
        msg = element.text
        logging.info(f'冒泡消息是:{msg}')
        # 返回消息文本
        return msg


    # 删除商品
    def delete_goods(self, good_name):
        # 对指定商品删除
        # 注意这里没法对定位提取成类变量，因为删掉的商品名不固定
        self.do_find(By.XPATH,f"//*[text()='{good_name}']/../..//*[text()='删除']").click()
        # 跳转到当前页
        return  GoodsListPage(self.driver)


    """类目列表页面：获取操作结果"""
    def get_delete_result(self):
        # 获取冒泡消息文本
        element = self.wait_element_until_visible(self.__MSG_DELETE_OPERATE)
        # 消息文本
        msg = element.text
        logging.info(f'冒泡消息是:{msg}')
        # 返回消息文本
        return msg