class Employee:
    def __init__(self, name, age, position, salary):
        # Store all details in one variable (dictionary)
        self.details = {
            "name": name,
            "age": age,
            "position": position,
            "salary": salary
        }

        self.status = "Pending"
        self.reason = None

    def accept(self):
        self.status = "Accepted"
        self.reason = "Meets requirements"
        print(f"{self.details['name']} has been ACCEPTED.")

    def reject(self, reason="Does not meet requirements"):
        self.status = "Rejected"
        self.reason = reason
        print(f"{self.details['name']} has been REJECTED. Reason: {reason}")

    def get_info(self):
        # Return all details + decision
        info = self.details.copy()
        info["status"] = self.status
        info["reason"] = self.reason
        return info
emp = Employee("Alice", 28, "Software Engineer", 75000)

emp.accept()

print(emp.get_info())