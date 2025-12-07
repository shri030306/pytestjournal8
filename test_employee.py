from employee import employee_details

def test_employee_details():
    expected_output = (
        "Employee Name: Shreesai\n"
        "Employee ID: 0318\n"
        "Department: HR\n"
        "Salary: 55000"
    )
    assert employee_details("Shreesai", "0318", "HR", 56000) == expected_output