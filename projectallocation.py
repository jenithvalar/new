from selenium.webdriver.common.by import By
from helper.seleniumhelper import SeleniumHelper


class ProjectAllocation(SeleniumHelper):
    previous_right = (By.XPATH, '//span[@class="fa fa-caret-right"]')
    no_project = (By.XPATH, '//*[text()="Resource Pool - Resource Pool"]')

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def test_project_allocation(self, Project):
        try:
            self.element_click(self.previous_right)
            self.element_is_present(self.no_project)
            project_txt = self.get_element_text(self.no_project)
            print(project_txt)

            if project_txt == Project:
                project_report = "Your not allocated to any project"
                self.write_report_to_file(project_report,
                                          r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\no_project.txt")

            else:
                project_report = "Your allocated to any project"
                self.write_report_to_file(project_report,
                                          r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\report\project.txt")

        except Exception as e:
            print(f"An error occurred: {e}")
