from selenium.webdriver.support.wait import WebDriverWait
from page_objects.base_page import BasePage
from selenium.webdriver.common.by import  By
from utils.web_util import click_exception


# 商品创建页面


class GoodCreatePage(BasePage):


    def create_good(self):
        # 输入商品编号
        self.driver.find_element(By.XPATH,"//*[@class='el-form']/div[1]//input").send_keys('000000001')
        # 输入商品名称
        self.driver.find_element(By.XPATH,"//*[@class='el-form']/div[2]//input").send_keys('新增商品测试')
        # 智能等待按钮点击状态
        # 点击上架
        WebDriverWait(self.driver,10).until(click_exception(By.XPATH,"//span[text()='上架']"))
        # self.driver.find_element(By.XPATH,"//span[text()='上架']").click()
        # 返回商品列表
        from page_objects.good_list_page import GoodsListPage
        return GoodsListPage(self.driver)

