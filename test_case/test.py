from page_objects.login_page import LoginPage

class TestLitemall:
    # 前置操组
    def setup_class(self):
        # 登录页面：用户登录，跳转到首页
        self.home = LoginPage().login()


    def test_add_type(self):
        """类目列表页面：点击添加"""
        """创建类目页面：创建类目"""
        """类目列表页面：获取操作结果"""
        res = (self.home
               .go_to_goods()
               .click_add()
               .create_good()
               .get_operate_result()
        )
        assert  '创建成功' == res


