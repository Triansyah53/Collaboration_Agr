from Collaboration_Agr.src.Pages.Locators.loginLocators import loginLocator
from Collaboration_Agr.src.SeleniumExtended import SeleniumExtended
from Collaboration_Agr.src.helpers.config_helper import get_base_url
import logging as logger
class loginPage(loginLocator):
    endpoint = '/login/'
    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def go_to_login_page(self):
        base_url=get_base_url()
        login_url=base_url
        logger.info(f"Going to {login_url}")
        self.driver.get(login_url)
    def login(self):
        self.sl.wait_and_input_text(self.USERNAME_FIELD_L,self.USERNAME)
        self.sl.wait_and_input_text(self.PASSWORD_FIELD_L,self.PASSWORD)
        self.sl.wait_and_click(self.LOGIN_BUTTON_L)


    def is_login_succesfull(self):
        self.sl.wait_until_element_contains_text(self.LOGIN_ASSERT_L, 'Dashboard')

    def login_plus_assert(self):
        self.login()
        self.is_login_succesfull()


