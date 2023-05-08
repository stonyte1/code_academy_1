import os

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

class Loan():
    def __init__(self, loan, period, annual_interest_rate=8):
        self.loan = loan
        self.annual_interest_rate = annual_interest_rate
        self.period = period
    
    @property
    def month_interest_rate(self):
        '''Gives monthly annual increse'''
        annual_increase = self.loan * (self.annual_interest_rate / 100) * self.period / 12
        return float(annual_increase)
    
    @property
    def month_sum_increase(self):
        mothly_increase = self.month_interest_rate + self.loan
        return float(mothly_increase)
    
    @property
    def year_interest_rate(self):
        '''Gives yearly annual increse'''
        annual_increase = self.loan * (self.annual_interest_rate / 100) * self.period
        return float(annual_increase)
    
    @property
    def year_sum_increase(self):
        year_increase = self.year_interest_rate + self.loan
        return float(year_increase)


if __name__ == '__main__':
    clear()
    print('----Loan calculator----')

    loan = float(input('Enter your loan: '))
    period = float(input('Enter your loan period: '))
    annual_interest_rate = input('Press 1 to input annual rate if no press 0: ')
    
    if annual_interest_rate == '1':
        annual_interest_rate = float(input('Enter annual rate: '))  
        user = Loan(loan, period, annual_interest_rate)
    else:
        user = Loan(loan, period)
    
    while True:
        try:
            month_year = input('Monthly or yearly rate: ')
        except ValueError as err:
            month_year = input('Wrong input write monthly or yearly: ')
        clear()

        if month_year == 'monthly':
            print(f'Monthly interest rate: {user.month_interest_rate}, sum: {user.month_sum_increase}')
        else:
            print(f'Yearly imterest rate: {user.year_interest_rate}, sum: {user.year_sum_increase}')
        
        end = input('To stop calcultor press enter: ')
        if end == '':
            clear()
            break



