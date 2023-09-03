from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By
import logging

# 首页
class HomePage(BasePage):

    __MENU_GOOD_MANAGE = (By.XPATH, "//*[text()='商品管理']")
    __MENU_GOOD_LIST = (By.XPATH, "//*[text()='商品列表']")

    # 公共方法
    """系统首页：进入商品列表"""
    def go_to_goods(self):
        logging.info('进入商品列表')
        #点击菜单“商品管理”
        self.do_find(self.__MENU_GOOD_MANAGE).click()
        # 点击菜单“商品列表”
        self.do_find(self.__MENU_GOOD_LIST).click()
        # 返回商品列表页面
        from page_objects.good_list_page import GoodsListPage
        return GoodsListPage(self.driver)

