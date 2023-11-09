import pytest
from selenium.webdriver.common.by import By
from helper.seleniumhelper import SeleniumHelper
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddActivity(SeleniumHelper):
    dropdown_arrow = (By.XPATH, '//span[@class="select2-selection__arrow"]')
    dropdown_options = (By.CSS_SELECTOR, 'ul.select2-results__options li')

    def test_Add_activity(self, activity):
        try:
            self.element_click(self.dropdown_arrow)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.dropdown_options))
            dropdown_elements = self.driver.find_elements(*self.dropdown_options)

            activity_found = False

            for element in dropdown_elements:
                if element.text == activity:
                    element.click()
                    activity_report = 'The activity you wanted to select is selected successfully'
                    self.write_report_to_file(activity_report,
                                              r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\activity_dropdown.txt")
                    activity_found = True
                    break

            if not activity_found:
                print(f"The activity '{activity}' was not found in the dropdown.")

        except Exception as e:
            pytest.fail(f"An error occurred in choose_activity_by_text: {e}")
