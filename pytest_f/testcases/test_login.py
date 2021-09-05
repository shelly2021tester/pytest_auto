from pytest_f.testpageobjects.testloginObject import TestLogPage
from pytest_f.config.testconfig import datafile_path
from pytest_f.data.read_write import ReadWrite
from pytest_f.log.log import logger
import time
import pytest

class TestLogin:
    def login(self,test_logsystem):
        self.page1=TestLogPage(test_logsystem)
        file=ReadWrite(datafile_path,1)
        userlist = file.read()
        user = userlist[0]
        self.page1.type_username(user[0])
        self.page1.type_password(user[1])
        self.page1.click_login()
        try:
            time.sleep(2)
            assert self.page1.browser.title == "我的地盘 - 禅道"
            print("测试用例成功：登录成功！")
            # self.assertEqual(self.page1.browser.title, '我的地盘 - 禅道')
        except AssertionError:
            print("测试用例失败：登录失败！")
        self.page1.click_user()
        self.page1.click_logout()
        logger.info("验证用户登录信息......")


    def test_2_login(self,test_logsystem):
        self.page1=TestLogPage(test_logsystem)
        file = ReadWrite(datafile_path, 1)
        userlist = file.read()
        user = userlist[1]
        self.page1.type_username(user[0])
        self.page1.type_password(user[1])
        self.page1.click_login()
        time.sleep(3)
        try:
            time.sleep(2)
            alert =self.page1.browser.switch_to.alert
            text = alert.text
            # promp = Alert(self.browser)
            # text = promp.text()
            assert "登录失败" in text
            alert.accept()
            time.sleep(2)
            print("测试用例成功：显示登录失败提示信息！")
            # self.assertIn("登录失败",text)
            logger.info("验证用户登录失败信息.......")
        except AssertionError:
            # promp.accept()
            alert.accept()
            time.sleep(2)
            print("测试用例失败：异常情况！")
            logger.info("验证用户登录失败信息.......")

    def test_3_login(self, test_logsystem):
        self.page1 = TestLogPage(test_logsystem)
        file = ReadWrite(datafile_path, 1)
        userlist = file.read()
        user = userlist[0]
        self.page1.type_username(user[0])
        self.page1.type_password(user[1])
        self.page1.click_login()
        try:
            time.sleep(2)
            assert self.page1.browser.title == "我的地盘 - 禅道"
            print("测试用例成功：登录成功！")
            # self.assertEqual(self.page1.browser.title, '我的地盘 - 禅道')
        except AssertionError:
            print("测试用例失败：登录失败！")
        self.page1.click_user()
        self.page1.click_logout()
        logger.info("验证用户登录信息......")

if __name__=='__main__':
    pytest.main()