#If the name changes it will update the Method results
class Employee:

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

#This Method returns their email address
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

#This Method returns their full name
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

#This Method will give them a raise of  5%
    @property
    def apply_raise(self):
        self.pay = int(self.pay) * self.raise_amt)