from selenium.webdriver.common.by import By

from pages.loginpage import LoginPage


class LogoutPage(LoginPage):
    email_input = (By.XPATH, '//input[@type="email"]')
    password_input = (By.XPATH, '//input[@type="password"]')
    login_button = (By.XPATH, '//input[@id="submitbtn"]')
    profile_button = (By.XPATH, '//li[@class="nav-item dropdown"]')
    logout_button = (By.XPATH, '//button[@type="submit"]')
    dashboard = (By.XPATH, '//span[text()="Dashboard"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_logout(self, email, password):
        user_input = input("Do you want to log out? (yes/no): ")
        if user_input.lower() == 'yes':
            profile_button = self.is_element_displayed(self.profile_button)
            assert profile_button, "Profile dropdown button is not displayed"
            self.element_click(self.profile_button)

            logout_success = self.is_element_displayed(self.logout_button)
            assert logout_success, "Logout was not successful"
            self.element_click(self.logout_button)

            logout_success = self.wait_for_element_to_be_present(self.login_button, timeout=5)
            report_logout = "The Logout was Successful"
            if logout_success:
                self.write_report_to_file(report_logout,
                                          r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\logout.txt")

            user_input2 = input("Do you want to login again? (yes/no): ")
            if user_input2.lower() == 'yes':
                self.test_aspire_login(email, password)
                re_login_success = self.wait_for_element_to_be_present(self.profile_button, timeout=5)
                re_login = "The Re-Login was Successful"
                if re_login_success:
                    self.write_report_to_file(re_login,
                                              r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\relogin.txt")

                    dashboard_text = self.get_element_text(self.dashboard)
                    if dashboard_text == 'Dashboard':
                        dashboard_nav = "The text is matched. You are navigated to the dashboard"
                        self.write_report_to_file(dashboard_nav,
                                                  r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\dashboard_nav.txt")
                    else:
                        dashboard_error = "The text is not matched. You missed navigating to the dashboard"
                        self.write_report_to_file(dashboard_error,
                                                  r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\dashboard_error.txt")
                elif user_input2.lower() == 'no':
                    print("Just stay out.")
                else:
                    print("Invalid input. Please enter 'yes' or 'no.")
        elif user_input.lower() == 'no':
            print("Just stay in.")
        else:
            print("Invalid input. Please enter 'yes' or 'no.")
