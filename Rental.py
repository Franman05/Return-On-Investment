 class Rental_Property():

    def Income(self):
        self.rental = 1700
        # Total monthly rent payments on Property

    def monthly_expenses(self):
        self.taxes = 100
        self.insurance = 100
        self.vacancy = 75
        self.repairs = 50
        self.mortage = 650
        self.lawn = 100
    
    def total_monthly_expenses(self):
        print('TOTAL EXPENSES IS' + self.taxes + self.insurance + self.vacancy + self.repairs + self.mortage + self.lawn)
        # Total monthly expenses on Property

    def cash_flow(Income, total_monthly_expenses):
        print(Income - total_monthly_expenses)
        # Total monthly cash flow coming back to you

    def Investments(self):
        self.down_payment = 30000
        self.closing_cost = 1500
        self.pre_fixes = 3000
        print(self.down_payment * self.closing_cost * self.pre_fixes)
        # Total Investment into Property

    def annual_cash_flow(cash_flow):
        print(cash_flow * 12)
        # Total annual cash cash_flow

    def Cash_On_Cash(annual_cash_flow, Investments):
        print(annual_cash_flow * Investments)
        # Return on Investment(ROI) for Property

ROI = Rental_Property()
ROI.Cash_On_Cash(7500*34500)

