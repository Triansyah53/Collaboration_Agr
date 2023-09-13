from selenium.webdriver.common.by import By


class loginLocator:
    USERNAME_FIELD_L=(By.ID,'username')
    PASSWORD_FIELD_L=(By.ID,'password')
    LOGIN_BUTTON_L=(By.ID,'loginButton')
    LOGIN_ASSERT_L=(By.CLASS_NAME,'breadcrumb-item')

    USERNAME=''
    PASSWORD=''
