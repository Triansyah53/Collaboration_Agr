from Collaboration_Agr.src.SeleniumExtended import SeleniumExtended
from Collaboration_Agr.src.helpers.config_helper import get_base_url
from Collaboration_Agr.src.Pages.Locators.NavigationLocators import NavigationLocators
class NavigationPage(NavigationLocators):
    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)



