import pdb
import time

from Collaboration_Agr.src.Pages.NavigationPage import NavigationPage
from Collaboration_Agr.src.Pages.loginPage import loginPage
from Collaboration_Agr.src.Pages.ProgramPage import ProgramPage


import pytest

@pytest.mark.usefixtures('init_driver')
class TestCreateProgram():
    @pytest.mark.program
    def test_create_program(self):
        login = loginPage(self.driver)
        navigation_p = NavigationPage(self.driver)
        program_p= ProgramPage(self.driver)


        login.go_to_login_page()
        login.login()
        login.is_login_succesfull()
        navigation_p.choose_docstore()
        navigation_p.go_to_program_menu()
        program_p.add_program()
        program_p.program_detail()
        program_p.choose_currencies()
        time.sleep(10)
