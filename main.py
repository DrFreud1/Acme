from app.employee import Employee
from app.payment_manager import PaymentManager
from config import INPUT_FILE_PATH

if __name__ == "__main__":
    pm = PaymentManager()
    employees = Employee.load_shifts(INPUT_FILE_PATH)
    for employee in employees:
        pm.update_balance(employee)
        print(f"The amount to pay {employee.name} is: {employee.credit} USD")
