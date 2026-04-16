## What I am doing:
automate the following workflows using the Page Object Model (POM) in the Orange HRM web application.
Website: https://opensource-demo.orangehrmlive.com/web/index.php/auth/login (The login credentials are provided on the page.)
Automation Workflow:
1. Automate the Login Flow.
2. Navigate to the PIM module:
○ After logging in, the mouse hovers over PIM and clicks on it.
3. Add Employees:
○ On the PIM page, click on "Add Employee" and add 3-4 employees.
4. Verify Employees in the Employee List:
○ Navigate to the "Employee List" page.
○ Scroll through the list and locate the employees added.
○ Verify their names and print "Name Verified" once found.
5. Log Out from the Dashboard.

## About:
This project contains automation test scripts using Selenium (Python).

## Tools Used:
- Selenium
- Python
- Pytest

## How to run:
1. Install dependencies
2. Run test files using pytest
