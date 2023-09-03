from selenium.webdriver.support.wait import WebDriverWait
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import  By
from utils.web_util import click_exception
import logging

# 商品创建页面


class GoodCreatePage(BasePage):

    __INPUT_GOOD_CODE = (By.XPATH,"//*[@class='el-form']/div[1]//input")
    __INPUT_GOOD_NAME = (By.XPATH,"//*[@class='el-form']/div[2]//input")
    __BIT_CONFIRM = (By.XPATH,"//span[text()='上架']")

    def create_good(self,good_name):
        # 输入商品编号
        self.driver.find_element(By.XPATH,"//*[@class='el-form']/div[1]//input").send_keys('000000001')
        self.do_send_keys('000000001',self.__INPUT_GOOD_CODE)
        # 输入商品名称
        self.do_send_keys(good_name,self.__INPUT_GOOD_NAME)
        # 智能等待按钮点击状态
        # 点击上架
        # click_exception处用了元组解包 *，这是因为原本是需要两个参数的，上方变量__BIT_CONFIRM是一个元组
        WebDriverWait(self.driver,10).until(click_exception(*self.__BIT_CONFIRM))
        # 返回商品列表
        from page_objects.good_list_page import GoodsListPage
        return GoodsListPage(self.driver)

