import pytest
from selenium import webdriver


# Agile Project Management,Code Review,Coimbatore Holiday,Comp off,Customer Meeting,Customer Support
# Daily scrum,Development,Documentation/Reports,Election Leave,General admin,GRC Activities- Customer Support
# Internal Meeting,Interview,Learning & Development,Leave,Scrum Activities,Sprint Planning,Sprint Retrospective
# Status Reporting,Testing,Training


@pytest.fixture(scope="session")
def base_url():
    return "https://aspire.atmecs.online/login"


@pytest.fixture(scope="session")
def timesheet_data():
    return {
        "email": "jenith.ravichandran@atmecs.com",
        "password": "Jenithvarma@123",
        "text": "I worked on all the five days",
        "activity": "Learning & Development",
        "values": [9, 9, 9, 9, 9],
        "current_date_text": "06/11 - 12/11",
        "previous_date_text": "30/10 - 05/11",
        "Project": "Resource Pool - Resource Pool",

    }


@pytest.fixture(scope="session", autouse=True)
def browser_setup():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    yield driver

# @pytest.fixture(scope="session")
# def driver_setup():
#     chrome_options = webdriver.ChromeOptions()
#     driver = webdriver.Chrome(options=chrome_options)
#     yield driver
