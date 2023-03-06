import unittest
from time import sleep
from selenium import webdriver

class BaseUtil(unittest.TestCase):
    def setUp(self) :  # 启动浏览器等初始化步骤
        self.driver = webdriver.Chrome()
        global driver
        driver=self.driver
        self.driver.implicitly_wait(15)  # 隐式等待15秒
        self.driver.get("http://101.52.140.73/mweb/#/m2vop/index") #打开待测试网址
        self.driver.maximize_window()
        sleep(3)

    def tearDown(self):
        pass
        sleep(3)  # 强制等待3s
        self.driver.quit()

    # @classmethod
    # def setUpClass(cls) :  # 启动浏览器等初始化步骤
    #     cls.driver = webdriver.Chrome()
    #     global driver
    #     driver=cls.driver
    #     cls.driver.implicitly_wait(15)  # 隐式等待15秒
    #     cls.driver.get("http://101.52.140.73/mweb/#/m2vop/index") #打开待测试网址
    #     cls.driver.maximize_window()
    #     sleep(3)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     pass
    #     sleep(3)  # 强制等待3s
    #     cls.driver.quit()
