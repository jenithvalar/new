import pytest

# pytest --junit-xml=junitXMLReport.xml

if __name__ == "__main__":
    pytest.main([
        "-s", r"C:\Users\jenith.ravichandran\PycharmProjects\TimesheetAutomation\TestRun\test_suite.py",
        "--html=report.html"
    ])
