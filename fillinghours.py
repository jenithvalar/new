from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from helper.seleniumhelper import SeleniumHelper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FillingHours(SeleniumHelper):
    hours = (By.XPATH, '//td[@class=" workhourstd"]//input')
    leave_hours0 = (By.XPATH, '(//input[@class="form-control width-60 workhours hasaccessto"])[7]')
    leave_hours1 = (By.XPATH, '(//input[@class="form-control width-60 workhours hasaccessto"])[8]')
    leave_hours2 = (By.XPATH, '(//input[@class="form-control width-60 workhours hasaccessto"])[9]')
    leave_hours3 = (By.XPATH, '(//input[@class="form-control width-60 workhours hasaccessto"])[10]')
    leave_hours4 = (By.XPATH, '(//input[@class="form-control width-60 workhours hasaccessto"])[11]')
    add_activity = (By.XPATH, '//button[@class="addmore btn btn-sm btn-success "]')
    drop_down_button2 = (By.XPATH, '(//span[@class="select2-selection__arrow"])[2]')
    leave = (By.XPATH, '//li[text()="Leave"]')
    activity = (By.XPATH, '//li[@class="select2-results__option"]')
    save = (By.XPATH, '//a[text()="Save"]')
    ok_button = (By.XPATH, '//div[@class="modal-content"]/div[@class="modal-footer"]/button')
    notes = (By.XPATH, '//button[@class="notes-pop btn btn-sm btn-info"]')
    text = (By.XPATH, '(//div[@class="form-group"]//following::textarea[@class="form-control notetext"])[2]')
    text_ok_button = (By.XPATH, '(//button[@class="btn btn-sm btn-primary save-notes"])[2]')
    delete_activity = (By.XPATH, '//button[@class="removefield btn btn-sm btn-danger"]')

    def filling_timesheet_hours(self, values, text):
        try:
            self.element_is_present(self.notes)
            self.element_click(self.notes)
            self.is_element_displayed(self.text)
            self.element_enter(self.text, text)

            self.element_click(self.text_ok_button)

            index_of_zero = values.index(0)
            print(f"The value 0 is at index {index_of_zero}.")
        except ValueError:
            print("The value 0 is not present in the list.")
            index_of_zero = -1

        elements = self.find_elements(self.hours)

        for i, element in enumerate(elements):
            value_to_insert = values[i]
            element.clear()
            element.send_keys(str(value_to_insert))

        if index_of_zero == -1:
            self.element_click(self.save)
            timesheet_hours = 'The time sheet hours are filled for 5 days for a total of 45 hours'
            self.write_report_to_file(timesheet_hours,
                                      r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\full_hours.txt")

            if index_of_zero < 9:
                try:
                    wait = WebDriverWait(self.driver, 10)
                    wait.until(EC.invisibility_of_element_located((By.ID, "alertPopup")))
                    self.element_click(self.ok_button)
                    less_hours = 'The time sheet hours are filled less than 45 hours and it is saved'
                    self.write_report_to_file(less_hours,
                                              r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\less_hours.txt")
                except TimeoutException:
                    print("The alert popup did not disappear within the expected time.")

        else:
            try:

                wait = WebDriverWait(self.driver, 10)
                add_activity_button = wait.until(EC.element_to_be_clickable(self.add_activity))
                self.element_click(add_activity_button)
                add_activity = 'The new activity is added successfully'
                self.write_report_to_file(add_activity,
                                          r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\add_activity.txt")

                wait = WebDriverWait(self.driver, 10)
                drop2 = wait.until(EC.element_to_be_clickable(self.drop_down_button2))
                drop2.click()
                self.element_click(self.leave)

                leave_hours = [self.leave_hours0, self.leave_hours1, self.leave_hours2, self.leave_hours3,
                               self.leave_hours4]
                if 0 <= index_of_zero < len(leave_hours):
                    leave_element = leave_hours[index_of_zero]
                    self.scroll_into(leave_element)
                    self.element_click(leave_element)
                    self.element_clear(leave_element)
                    self.element_enter(leave_element, "L")
                    self.element_click(self.save)
                    self.element_click(self.ok_button)
                    leave_applied = 'Leave is applied successfully and it is saved successfully'
                    self.write_report_to_file(leave_applied,
                                              r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\leave.txt")

                else:
                    print("There is no 0 is present")
                    self.element_click(self.save)
                    self.element_click(self.ok_button)

                    no_leave_applied = 'Leave is applied successfully'
                    self.write_report_to_file(no_leave_applied,
                                              r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\no_leave.txt")
            except TimeoutException:
                print("The alert popup did not disappear within the expected time.")
