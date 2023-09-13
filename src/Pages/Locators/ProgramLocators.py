from selenium.webdriver.common.by import By
import random


class ProgramLocators:
    ADD_PROGRAM_BUTTON_L = (By.CSS_SELECTOR, 'button.btn-primary i.fa-plus')
    PROGRAM_NAME_FIELD_L = (By.NAME, 'name')
    PROGRAM_DESC_FIELD_L = (By.NAME, 'description')
    CURRENCIES_L = (By.XPATH, '//div[contains(text(),"Type to Select")]')
    INPUT_CURRENCIES_L = (By.XPATH, '//form/div[3]/div[2]/div/div[1]/div[1]/div/div/input')
