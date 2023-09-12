from selenium import webdriver
from selenium.webdriver.common.by import By
from Collaboration_Agr.src.SeleniumExtended import SeleniumExtended
from Collaboration_Agr.src.helpers.config_helper import get_base_url
from Collaboration_Agr.src.Pages.Locators.NavigationLocators import NavigationLocators
from Collaboration_Agr.src.Pages.Locators.ProgramLocators import ProgramLocators
from selenium.webdriver.common.keys import Keys

class ProgramPage(ProgramLocators):
    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def add_program(self):
        self.sl.wait_and_click(self.ADD_PROGRAM_BUTTON_L)