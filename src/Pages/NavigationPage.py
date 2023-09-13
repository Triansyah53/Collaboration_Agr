import pdb
import time

from Collaboration_Agr.src.SeleniumExtended import SeleniumExtended
from Collaboration_Agr.src.Pages.Locators.NavigationLocators import NavigationLocators
from selenium.webdriver.common.keys import Keys
class NavigationPage(NavigationLocators):
    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def choose_docstore(self):
        self.sl.wait_and_click(self.DOCSTORE_L)
        self.sl.wait_and_input_text(self.DOCSTORE_FIELD_L, "DUMMY BUYER")
        time.sleep(1)
        self.driver.find_element(*self.DOCSTORE_FIELD_L).send_keys(Keys.ENTER)
        time.sleep(1)

    def go_to_program_menu(self):
        self.sl.wait_and_click(self.MENU_ADMINISTRATON_L)
        self.sl.wait_and_click(self.SUBMENU_PROGRAM_L)








