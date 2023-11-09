from selenium.webdriver.common.by import By
from helper.seleniumhelper import SeleniumHelper


class Timesheetpage(SeleniumHelper):
    timesheet = (By.XPATH, '(//a[@class="sidebar-link"])[6]')
    timesheet_header = (By.XPATH, '//section[@class="content-header tms-content-header"]')
    date_element = (By.XPATH, '//b[@class="mt-2"]')
    week_off = (By.XPATH, '//h3[text()="WO - Week off"]')
    holiday = (By.XPATH, '//h3[text()="H - Holiday"]')
    Leave = (By.XPATH, '//h3[text()="L - Leave"]')
    date = (By.XPATH, '//b[@class="mt-2"]')

    def test_timesheet_navigation(self):
        self.element_click(self.timesheet)

        if self.element_is_present(self.timesheet_header):
            header = "Your in the Timesheet page"
            self.write_report_to_file(header,
                                      r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\Timesheet_nav.txt")

        else:
            header = "Your are not in the Timesheet page"
            self.write_report_to_file(header,
                                      r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\Timesheet_error.txt")

    def test_current_week(self, current_date_text):
        self.element_is_present(self.date)
        date_txt = self.get_element_text(self.date)
        date_parts = date_txt.split(':')
        if len(date_parts) == 2:
            date_range = date_parts[1].strip()

            if date_range == current_date_text:
                current_week_report = "You are in the current week Timesheet"
                self.write_report_to_file(current_week_report,
                                          r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\current_week_timesheet.txt")
            else:
                print("You are not in the current week")
        else:
            print("Date format not as expected")

    def test_timesheet_labels(self):
        wo_text = self.get_element_text(self.week_off)
        if wo_text == "WO - Week off":
            wotext = "The Week_off label is present in the Timesheet"
            self.write_report_to_file(wotext,
                                      r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\wo_label.txt")

        else:
            wotext2 = "The Week_off label is not present in the Timesheet"
            self.write_report_to_file(wotext2,
                                      r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\wo_label_error.txt")

        ho_text = self.get_element_text(self.holiday)
        if ho_text == "H - Holiday":
            hotext = "The Holiday label is present in the Timesheet"
            self.write_report_to_file(hotext,
                                      r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\ho_label.txt")

        else:
            hotext2 = "The Holiday label is not present in the Timesheet"
            self.write_report_to_file(hotext2,
                                      r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\ho_label_error.txt")

        l_text = self.get_element_text(self.Leave)
        if l_text == "L - Leave":
            Ltext = "The Leave label is present in the Timesheet"
            self.write_report_to_file(Ltext,
                                      r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\l_label.txt")

        else:
            Ltext2 = "The Leave label is not present in the Timesheet"
            self.write_report_to_file(Ltext2,
                                      r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\L_label_error.txt")
