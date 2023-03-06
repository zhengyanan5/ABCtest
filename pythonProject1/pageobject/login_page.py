import logging

import self as self
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from common.picturepro import imagepro
from time import sleep
from base.base_log import Log


class LoginPage(BasePage):

    #页面元素
    username_loc=(By.XPATH, '/html/body/div[1]/div/div[2]/div/form/div[1]/div/div/input')
    password_loc=(By.XPATH, '/html/body/div[1]/div/div[2]/div/form/div[2]/div/div/input')
    certif_loc=(By.XPATH, '/html/body/div/div/div[2]/div/form/div[3]/div/div/input')
    user_click=(By.XPATH, '/html/body/div/div/div[2]/div/form/div[4]/div/button')
    mes_loc=(By.XPATH,'/html/body/div/div/div[2]/div/form/div[1]/div/div/input')
    login_click=(By.XPATH,'/html/body/div/div/div[2]/div/form/div[2]/div/button')

    web01_loc=(By.XPATH,'/html/body/div/div/section/div/div[2]/div/div/div/div[2]/div[1]/div/div')

    #断言元素
    assert_x=(By.XPATH,'/html/body/div/div/div/header/div[1]/div/div/span')
    assert_y = (By.XPATH, '/html/body/div/div/section/div/div/div/aside/ul/div/li[1]/div/span')

    #页面动作
    def login(self, input_username, input_password,input_certif):
        self.send_keys(LoginPage.username_loc,input_username)
        self.send_keys(LoginPage.password_loc,input_password)
        self.send_keys(LoginPage.certif_loc,input_certif)
        self.click(LoginPage.user_click)

    def login_mes(self,input_mes):
        self.send_keys(LoginPage.mes_loc,input_mes)
        self.click(LoginPage.login_click)


    def web01(self):
        self.click(LoginPage.web01_loc)

    #断言(获取预期结果)
    def get_except_result(self):
        return self.get_value(LoginPage.assert_x)

    def get_except_result01(self):
        return self.get_value(LoginPage.assert_y)

    '''登陆'''
    def login_w(self):
        # print(result)
        username = 'AAA'
        password = 'OStem#2022'

        while '短信验证码' not in self.driver.page_source:
            self.driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div/form/div[3]/div/div/input').clear()
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/form/div[1]/div/div/input').clear()
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/form/div[2]/div/div/input').clear()
            l = BasePage(self.driver)
            l.get_screen()
            im = imagepro(self.driver)
            result = im.cro()
            log = Log()
            log.info("生成的验证码为："+result)
            certif = result
            print(certif)
            sleep(1)
            lp = LoginPage(self.driver)
            lp.login(username, password, certif)
            sleep(3)
        mes = '111111'
        lp = LoginPage(self.driver)
        lp.login_mes(mes)




