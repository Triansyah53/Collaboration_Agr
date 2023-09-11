import pytest
from Collaboration_Agr.src.Pages.loginPage import loginPage

@pytest.mark.usefixtures("init_driver")
class TestLogin:
    def test_login(self):
        login = loginPage(self.driver)
        login.go_to_login_page()
        login.login()
        login.is_login_succesfull()
