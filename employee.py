def employee_details(name, emp_id, department, salary):
    result = (
        f"Employee Name: {name}\n"
        f"Employee ID: {emp_id}\n"
        f"Department: {department}\n"
        f"Salary: {salary}"
    )
    return result

if __name__ == "__main__":
    name = "Shreesai"
    emp_id = "0318"
    department = "HR"
    salary = 56000

    print(employee_details(name, emp_id, department, salary))
