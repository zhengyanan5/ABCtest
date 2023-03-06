
#基础层：原生方法
class BasePage(object):
    #初始化方法，调用类执行，打开页面
    def __init__(self,driver):
        self.driver=driver

    #定位元素的关键字
    def locator_element(self,loc):
        return self.driver.find_element(*loc) #前面这个*，作用是解包

    #设置值的关键字
    def send_keys(self,loc,value):
        self.locator_element(loc).send_keys(value)

    #设置单击的关键字
    def click(self,loc):
        self.locator_element(loc).click()

    #清空关键字
    def clear_l(self,loc):
        self.locator_element(loc).clear()

    #获取关键字的文本值
    def get_value(self,loc):
        return self.locator_element(loc).text

    #截图
    def get_screen(self):
        self.driver.save_screenshot('screen.png')





