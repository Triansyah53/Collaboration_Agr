import pdb
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
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

    def choose_multiple_seller(self):
        self.sl.wait_and_click(self.ENABLE_SELLER_L)
        self.sl.wait_and_click(self.ENABLE_BUYER_L)
        self.sl.wait_and_click(self.ENABLE_MULTIPLE_BUYER_L)

    def choose_program_type(self):
        self.sl.wait_and_click(self.ENABLE_COLLABORATION_L)

    def fc_quote_settings(self):
        self.sl.wait_and_click(self.QS_ENABLED_L)
        self.sl.wait_and_click(self.QS_LITIGATION_L)
        self.sl.wait_and_click(self.QS_INVENTORY_CHECKING)
        self.sl.wait_and_click(self.QS_LINE_ITEM_REV)
        self.sl.wait_and_click(self.QS_DISCOUNT_APPROV)
        self.sl.wait_and_input_text(self.QS_LOGO_FIELD_L,'supplier')
        self.driver.find_element(*self.QS_LOGO_FIELD_L).send_keys(Keys.ENTER)

    def fc_order_settings(self):
        self.sl.wait_and_click(self.OS)
        self.sl.wait_and_click(self.OS_ENABLED_L)
        self.sl.wait_and_click(self.OS_LITIGATION_L)
        self.sl.wait_and_click(self.OS_LOGO_DROPDOWN_L)
        self.sl.wait_and_input_text(self.OS_LOGO_FIELD_L,'supplier')
        self.driver.find_element(*self.OS_LOGO_FIELD_L).send_keys(Keys.ENTER)

    def fc_despatch_advice_settings(self):
        self.sl.wait_and_click(self.DA)
        self.sl.wait_and_click(self.DA_PARTIAL_L)
        self.sl.wait_and_click(self.DA_DGOODS_CONFIRMATION_L)
        self.sl.wait_and_click(self.DA_INVEN_CHECK_L)
        self.sl.wait_and_click(self.DA_SIGNATURES_L)
        self.sl.wait_and_click(self.DA_ADD_SIGNATURES_L)
        self.sl.wait_and_click(self.DA_ADD_SIGNATURES_L)
        self.sl.wait_and_input_text(self.DA_SIGNATURES_FIELD_1,'Sender')
        self.sl.wait_and_input_text(self.DA_SIGNATURES_FIELD_2,'Receiver')
        self.sl.wait_and_click(self.DA_LOGO_DROPDOWN_L)
        self.sl.wait_and_input_text(self.DA_LOGO_FIELD_L,'supplier')
        self.driver.find_element(*self.DA_LOGO_FIELD_L).send_keys(Keys.ENTER)

    def fc_receive_advice(self):
        self.sl.wait_and_click(self.RA)
        self.sl.wait_and_click(self.RA_LOGO_DROPDOWN_L)
        self.sl.wait_and_input_text(self.RA_LOGO_FIELD_L,'buyer')
        self.driver.find_element(*self.RA_LOGO_FIELD_L).send_keys(Keys.ENTER)

    def fc_invoice(self):
        self.sl.wait_and_click(self.INV)
        self.sl.wait_and_click(self.INV_SIGNATURES_L)
        self.sl.wait_and_click(self.INV_ADD_SIGNATURES_L)
        self.sl.wait_and_input_text(self.INV_SIGNATURES_FIELD_L,'Board of Director')
        self.sl.wait_and_click(self.INV_LOGO_DROPDOWN_L)
        self.sl.wait_and_input_text(self.INV_LOGO_FIELD_L,'supplier')
        self.driver.find_element(*self.INV_LOGO_FIELD_L).send_keys(Keys.ENTER)

    def collab_cl(self):
        self.sl.wait_and_click(self.COLLABORATION_CL_L)

    def save_program(self):
        self.sl.wait_and_click(self.SAVE_PROGRAM_BUTTON_L)

    # def is_program_created(self):
    #     text=self.sl.wait_and_get_text(self.IS_PROGRAM_CREATED_L)

    def fc_full_settings(self):
        self.fc_quote_settings()
        self.fc_order_settings()
        self.fc_despatch_advice_settings()
        self.fc_receive_advice()
        self.fc_invoice()
        self.collab_cl()
        self.save_program()
        # self.is_program_created()


