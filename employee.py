"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    """
    contract params -
    1 = hours, 2 = pay/hour

    contract_commission params - 
    1 = num of contract commissions, 2 = pay/commission
    """
    def __init__(self, name, monthly_salary=0, bonus_commission=0, contract=[0, 0], contract_commission=[0, 0]):
        self.name = name
        self.monthly_salary = monthly_salary
        self.bonus_commission = bonus_commission
        self.contract = contract
        self.contract_commission = contract_commission
        self.pay = self.monthly_salary + self.bonus_commission + (self.contract[0] * self.contract[1]) + (self.contract_commission[0] * self.contract_commission[1])

    def get_pay(self):
        return self.pay

    def commission_info(self):
        commission_pay = ""
        if self.bonus_commission:
            commission_pay += f" and receives a bonus commission of {self.bonus_commission}."
        elif self.contract_commission[0]:
            commission_pay += f" and receives a commission for {self.contract_commission[0]} contract(s) at {self.contract_commission[1]}/contract."

        return commission_pay

    def __str__(self):
        payment_info = f"{self.name} works on a "

        if self.monthly_salary:
            payment_info += f"monthly salary of {self.monthly_salary}"

        elif self.contract[0]:
            payment_info = f"contract of {self.contract[0]} hours at {self.contract[1]}/hour"

        payment_info += self.commission_info()
        payment_info += f"  Their total pay is {self.pay}."
        return payment_info



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', monthly_salary=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', contract=[100, 25])

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', monthly_salary=3000, contract_commission=[4, 200])

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', contract=[150, 25], contract_commission=[3, 220])

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', monthly_salary=2000, bonus_commission=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', contract=[120, 30], bonus_commission=600)
