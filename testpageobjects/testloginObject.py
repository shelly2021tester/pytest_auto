from selenium.webdriver.common.by import By

class TestLogPage:
    def __init__(self,driver):
        self.username=By.NAME,'account'
        self.password=By.NAME,'password'
        self.submit=By.ID,'submit'
        self.browser=driver
        self.user=By.CSS_SELECTOR,"ul>li>.dropdown-toggle"
        self.logout=By.LINK_TEXT,'退出'

    def type_username(self,username):
        self.browser.find_element(*self.username).send_keys(username)

    def type_password(self,password):
        self.browser.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.browser.find_element(*self.submit).click()

    def click_user(self):
        self.browser.find_element(*self.user).click()

    def click_logout(self):
        self.browser.find_element(*self.logout).click()