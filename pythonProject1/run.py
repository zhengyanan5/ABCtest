import unittest
import HTMLTestRunner
import time
if __name__=='__main__':
    #执行需要的用例，并且生成html格式的自动化测试报告
    #使用unittest默认的测试用例的加载器去发现testcase目录下以py结尾的所有测试用例
    suite=unittest.defaultTestLoader.discover('./testcase','login.py')

    #now获取时间，以年-月-日，时-分-秒的格式，日期唯一性，保证日志名重复覆盖问题
    now=time.strftime("%Y-%m-%d %H_%M_%S")
    # now =str(int(time.time()))
    filename="./report/"+now+'result.html'

    #生成html报告文件
    report_file=open(filename,'wb')

    #生成一个HTMLTestRunner的运行器对象（必须下载一个HTMLTestRunner.py文件，放到指定目录）
    runner=HTMLTestRunner.HTMLTestRunner(stream=report_file, title='自动化测试报告')

    runner.run(suite)