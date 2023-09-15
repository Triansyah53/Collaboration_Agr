from selenium.webdriver.common.by import By


class loginLocator:
    USERNAME_FIELD_L = (By.ID, 'username')
    PASSWORD_FIELD_L = (By.ID, 'password')
    LOGIN_BUTTON_L = (By.ID, 'loginButton')
    LOGIN_ASSERT_L = (By.CLASS_NAME, 'breadcrumb-item')
    LOGIN_FAIL_MESSAGE_L = (By.XPATH, ('//span[text()="Failed to connect to the server, please try again."]'))

    USERNAME = ''
    PASSWORD = ''

