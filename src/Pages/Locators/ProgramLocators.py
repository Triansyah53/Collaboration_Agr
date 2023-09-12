from selenium.webdriver.common.by import By

class ProgramLocators:
    ADD_PROGRAM_BUTTON_L = (By.CSS_SELECTOR, 'button.btn-primary i.fa-plus')
    PROGRAM_NAME_FIELD_L = (By.NAME, 'name')
    PROGRAM_DESC_FIELD_L = (By.NAME, 'description')