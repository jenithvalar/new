import pytest

from TestRun.timesheettestrunner import TestTimesheetRunner


test_timesheet = pytest.mark.login

test_timesheet(TestTimesheetRunner.test_timesheet_functionality)


