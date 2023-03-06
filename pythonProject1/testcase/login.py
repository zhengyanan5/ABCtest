import ddt as ddt
from base.base_util import BaseUtil

from time import sleep

from pageobject.login_page import LoginPage


# @ddt.ddt
class TaskCase(BaseUtil):

    # 调用处理数据函数，*解包，数据处理过后分组传入用例
    # @ddt.data(*imagepro().cro())
    # @ddt.unpack
    def test_01_login(self):
        lw=LoginPage(self.driver)
        lw.login_w()

        # 断言
        self.assertIn('AAA', lw.get_except_result())

    def test_02_test1(self):

        lp = LoginPage(self.driver)
        lp.login_w()
        lp.web01()

        # 断言
        self.assertIn('清算管理', lp.get_except_result01())


