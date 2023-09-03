from page_objects.login_page import LoginPage

class TestLitemall:
    # 前置操组
    def setup_class(self):
        # 登录页面：用户登录，跳转到首页
        self.home = LoginPage().login()
    def teardown_class(self):
        # 退出浏览器
        self.home.do_quit()


    # 增加商品
    def test_add_good(self):
        """类目列表页面：点击添加"""
        """创建类目页面：创建类目"""
        """类目列表页面：获取操作结果"""
        res = self.home\
               .go_to_goods()\
               .click_add()\
               .create_good('新增商品测试')\
               .get_operate_result()

        assert  '创建成功' == res


    # 删除商品
    def test_delete_goods(self):
        # 对指定商品删除
        res = (self.home\
            .go_to_goods()\
            .click_add()\
            .create_good('删除商品测试')\
            .delete_goods('删除商品测试')\
            .get_delete_result())

        assert  '删除成功' == res




