class Category:
    def __init__(self,category,):
    # Instantiating the Category class with category and ledger parameter
        self.category = category
        self.ledger = []
        self.current_balance = 0
    # Creating the class methods
    def deposit(self,amount,description = ""):
    # Creating the format for inserting the amount and description
        deposit_form = dict()
        deposit_form["amount"] = (amount)
        deposit_form["description"] = description
        self.ledger.append(deposit_form)
    # Computing current balance
        self.current_balance += (amount)
    def withdraw(self,amount,description=""):
    # Creating the format for storing the amount in negative
    # And also checking if the wwithdraw took place or not depending on the current balance
        withdraw_form = dict()
    # Converting amount to negative form
        amount = 0 - amount
    # Chcekcing if amount withdrawn leaves the balance = 0 or < 0 or > 0
        if self.current_balance + amount == 0 or self.current_balance + amount > 0:
            withdraw_form["amount"] = (amount)
            withdraw_form["description"] = description
    # Appending to ledger
            self.ledger.append(withdraw_form)
    # Updating Current balance
            self.current_balance += (amount)
            return True
        else:
            return False
    
    def get_balance(self):
    # Retruning current balance
        return float("{:.2f}".format(self.current_balance))
    def transfer(self,amount,budget_category):
        # For the self.ledger 
        budget_category_1 = "Transfer to " + budget_category.category
        # For the recipient ledger
        budget_category_2 = "Transfer from " + self.category 
        deposit_form = dict()
        withdrawal_form = dict()
    # Setting the logic for the withdrawal
        amount = 0 - amount
        if self.current_balance + amount == 0 or self.current_balance + amount > 0:
            withdrawal_form["amount"] = (amount) 
            withdrawal_form["description"] = budget_category_1
            # Appending to self.ledger for withdrawal
            self.ledger.append(withdrawal_form)
            # Deposit into tanother category only if funds are sufficient from the other account
            deposit_form["amount"] = (-amount) # Minus added to change to positive
            deposit_form["description"] = budget_category_2
            budget_category.ledger.append(deposit_form)
            # Current balance for each ledger
            self.current_balance += (amount)
            budget_category.current_balance += (-amount) # Adding negative to turn it to positive because of the original-set up
            return True
        else:
            return False
    def check_funds(self,amount):
        if amount > self.current_balance:
            return False
        else:
            return True
    def __repr__(self):
        title = self.category.center(30,"*")
        line = "" 
        # Looping through ledger to format answer properly
        for i in self.ledger:
            line += "\n" + i["description"][:23].ljust(23) + "{:.2f}".format(i["amount"])[:7].rjust(7)
        # Returning formatted answer
        return title + line + "\n" + "Total: " + "{:.2f}".format(self.current_balance)
def create_spend_chart(categories):
    # Iterating through the categories list to get names and store in a list
    names_lst = []
    percent_lst = []
    withdrawal_lst = []
    for i in categories:
        names = i.category
        names_lst.append(names)
        # Computing percentages
        category_withdraw = 0
        for j in i.ledger:
            amount = round(float(j["amount"]))
            if amount < 0:
                category_withdraw += amount
        withdrawal_lst.append(-category_withdraw)
    withdraw_total = sum(withdrawal_lst)
    # Calculating percentage for each category
    for i in withdrawal_lst:
        percentage = (i*100)/withdraw_total
        percentage = round(percentage//10)*10
        percent_lst.append((percentage))
    # Designing the chart
    title = "Percentage spent by category"
    chart = ""
    for i in range(100,-10,-10):
        line = (str(i) + "|").rjust(4)
        for j in percent_lst:
            # Condition to print the "o" characters in the bar chart
            if j >= i:
                line += " o "
            else:
                line += "   " # Spaces between each categories on the chart if blank
        chart += "\n" + line + " "
    # Vertical category list
    new_lst = [] # Store new categories items with spaces for eqaul length
    max_len = len(max(names_lst,key=len)) # To get maximium length
    line = ""
    for i in names_lst: # Padding the values in the list with spaces to equal max len
        num_space = max_len - len(i)
        new_lst.append(i + (num_space*" "))
    for i in zip(*new_lst):
        line += "     " + "  ".join(i) + "  " + "\n"
    return title + chart + ("\n") + ((3*len(names_lst)+1)*"-").rjust(5+(3*len(names_lst))) + ("\n") + line.rstrip("\n")
food = Category("Food")
entertainment = Category("Entertainment")
business = Category("Business")
categories = [business,food,entertainment]
food.deposit(900,"deposit")
entertainment.deposit(900,"deposit")
business.deposit(900,"deposit")
print(food.withdraw(105.55))
print(entertainment.withdraw(34.44))
print(business.withdraw(10.99))
print(food.__repr__())
print(create_spend_chart(categories)) 


