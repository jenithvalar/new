from selenium.webdriver.common.by import By
from helper.seleniumhelper import SeleniumHelper


class PreviousWeekPage(SeleniumHelper):
    previous_left = (By.XPATH, '//span[@class="fa fa-caret-left "]')
    date = (By.XPATH, '//b[@class="mt-2"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_previous_week(self, previous_date_text):
        try:
            self.element_click(self.previous_left)
            self.element_is_present(self.date)
            date_txt1 = self.get_element_text(self.date)
            date_parts1 = date_txt1.split(':')
            if len(date_parts1) == 2:
                date_range1 = date_parts1[1].strip()
                if date_range1 == previous_date_text:
                    previous_week_report = "You are in the previous week Timesheet"
                    self.write_report_to_file(
                        previous_week_report,
                        r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\previous_week_timesheet.txt"
                    )
                else:
                    print("You are not in the previous week")
            else:
                print("Date format not as expected")
        except Exception as e:
            print(f"An error occurred: {e}")
