from page_objects.base_page import BasePage
from utils.logger_util import logger
from selenium.webdriver.common.by import By

# 首页
class HomePage(BasePage):

    # 公共方法
    """系统首页：进入商品列表"""
    def go_to_goods(self):
        logger.info('进入商品类目')
        #点击菜单“商品管理”
        self.driver.find_element(By.XPATH, "//*[text()='商品管理']").click()
        # 点击菜单“商品列表”
        self.driver.find_element(By.XPATH, "//*[text()='商品列表']").click()
        # 返回商品列表页面
        from page_objects.good_list_page import GoodsListPage
        return GoodsListPage(self.driver)

