import pytest

from pages.loginpage import LoginPage
from pages.logoutpage import LogoutPage
from pages.timesheetpage import Timesheetpage
from pages.previous_weekpage import PreviousWeekPage
from pages.projectallocation import ProjectAllocation
from pages.addactivity import AddActivity
from pages.fillinghours import FillingHours
from pages.comboff import CombOff


class TestTimesheetRunner:

    @pytest.fixture(autouse=True)
    def setup_class(self, browser_setup, base_url, timesheet_data):
        self.driver = browser_setup
        self.driver.get(base_url)

        self.login_page = LoginPage(self.driver)
        self.logout_page = LogoutPage(self.driver)
        self.timesheet_page = Timesheetpage(self.driver)
        self.previous_week = PreviousWeekPage(self.driver)
        self.project_allocation = ProjectAllocation(self.driver)
        self.add_activity = AddActivity(self.driver)
        self.filling_hours = FillingHours(self.driver)
        self.comboff = CombOff(self.driver)

        self.email = timesheet_data["email"]
        self.password = timesheet_data["password"]
        self.current_date_text = timesheet_data["current_date_text"]
        self.previous_date_text = timesheet_data["previous_date_text"]
        self.Project = timesheet_data["Project"]
        self.activity = timesheet_data["activity"]
        self.values = timesheet_data["values"]
        self.text = timesheet_data["text"]

    @pytest.mark.login
    def test_timesheet_functionality(self):
        try:

            self.login_page.test_aspire_login(self.email, self.password)

            self.logout_page.test_logout(self.email, self.password)

            self.timesheet_page.test_timesheet_navigation()

            self.timesheet_page.test_current_week(self.current_date_text)

            self.timesheet_page.test_timesheet_labels()

            self.previous_week.test_previous_week(self.previous_date_text)

            self.project_allocation.test_project_allocation(self.Project)

            self.add_activity.test_Add_activity(self.activity)

            self.filling_hours.filling_timesheet_hours(self.values, self.text)

        except Exception as e:
            pytest.fail(f"An error occurred: {e}")
