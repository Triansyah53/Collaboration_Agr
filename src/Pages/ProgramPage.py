import pdb

from Collaboration_Agr.src.SeleniumExtended import SeleniumExtended
from Collaboration_Agr.src.Pages.Locators.ProgramLocators import ProgramLocators
from Collaboration_Agr.src.helpers.generic_helper import generate_program_data

class ProgramPage(ProgramLocators):
    def __init__(self,driver):
        self.driver=driver
        self.sl=SeleniumExtended(self.driver)

    def add_program(self):
        self.sl.wait_and_click(self.ADD_PROGRAM_BUTTON_L)

    def program_detail(self,program_name=None,program_desc=None):
        if not program_name or not program_desc:
            program_data=generate_program_data()
            program_name = program_data['name']
            program_desc = program_data['description']
        self.sl.wait_and_input_text(self.PROGRAM_NAME_FIELD_L, program_name)
        self.sl.wait_and_input_text(self.PROGRAM_DESC_FIELD_L, program_desc)

    def choose_currencies(self):
        self.sl.wait_and_click(self.CURRENCIES_L)
        self.sl.wait_and_input_text(self.INPUT_CURRENCIES_L,'IDR')
        self.sl.send_enter_key(*self.INPUT_CURRENCIES_L)
