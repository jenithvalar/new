from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from helper.seleniumhelper import SeleniumHelper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CombOff(SeleniumHelper):
    hours = (By.XPATH, '//td[@class="workhourstd"]//input')
    hour0 = (By.XPATH, '(//input[@class="form-control width-60 workhours hasaccessto"])[7]')
    hour1 = (By.XPATH, '(//input[@class="form-control width-60 workhours hasaccessto"])[8]')
    hour2 = (By.XPATH, '(//input[@class="form-control width-60 workhours hasaccessto"])[9]')
    hour3 = (By.XPATH, '(//input[@class="form-control width-60 workhours hasaccessto"])[10]')
    hour4 = (By.XPATH, '(//input[@class="form-control width-60 workhours hasaccessto"])[11]')
    add_activity = (By.XPATH, '//button[@class="addmore btn btn-sm btn-success "]')
    drop_down_button2 = (By.XPATH, '(//span[@class="select2-selection__arrow"])[2]')
    activity = (By.XPATH, '//li[@class="select2-results__option"]')
    save = (By.XPATH, '//a[text()="Save"]')
    ok_button = (By.XPATH, '//div[@class="modal-content"]/div[@class="modal-footer"]/button')
    notes = (By.XPATH, '//button[@class="notes-pop btn btn-sm btn-info"]')
    text = (By.XPATH, '(//div[@class="form-group"]//following::textarea[@class="form-control notetext"])[2]')
    text_ok_button = (By.XPATH, '(//button[@class="btn btn-sm btn-primary save-notes"])[2]')
    delete_activity = (By.XPATH, '//button[@class="removefield btn btn-sm btn-danger"]')
    leave = (By.XPATH, '//li[text()="Leave"]')
    comb_off = (By.XPATH, '//li[text()="Comp off"]')
    Week_off = (By.XPATH, '(//input[@value="WO"])[3]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_Comb_Off_H(self, values):
        try:
            for index, hour in enumerate(self.find_elements(self.hours)):
                if "H" in hour.get_attribute(values):

                    add_activity = self.find_element(self.add_activity)
                    add_activity.click()

                    comb_xpaths = [self.hour0, self.hour1, self.hour2, self.hour3, self.hour4]

                    if index < len(comb_xpaths):
                        comb_xpath = comb_xpaths[index]
                        comb_element = self.find_element(comb_xpath)
                        comb_element.clear()
                        comb_element.send_keys("9")

        except TimeoutException:
            print("The hours element text H is not able to locate.")

    def test_Comb_Off_WO(self, values, text):
        try:
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
                wait = WebDriverWait(self.driver, 10)
                add_activity_button = wait.until(EC.element_to_be_clickable(self.add_activity))
                self.element_click(add_activity_button)
                weekoff_elemet = self.find_element(self.Week_off)
                weekoff_elemet.element_clear()
                self.element_enter(self.Week_off, "9")

        except TimeoutException:
            print("The week-off element WO text  is not able to locate.")
