"""
import math "library?"
print initial user output message "welcome message"
request calculation choice from user

"""

import math


welcome_message = input("investment - to calculate the amount of interest you'll earn on your investment \nbond       - to calculate the amount you'll have to pay on a home loan \n\nEnter either 'investment' or 'bond' from the menu above to proceed: ").lower()

print(welcome_message)

while True:
    try:

        if welcome_message == "investment":
            amount_of_money = float(input("Please enter the amount of money you would like to deposit: "))
            interest_rate = float(input("Please enter the interest rate, eg. for 10%, input 10: "))
            number_of_years = int(input("Please enter the number of years you plan on investing (to the nearest whole number: "))
            interest = input("Please enter the type of interest you would like, eg. 'simple' or 'compound': ").lower()
            p = amount_of_money
            r = interest_rate / 100
            t = number_of_years
            if interest == "simple":
                a = p * (1 + r * t)
                print(f"The amount of interest you'll earn on your home investment is: {a} !")
            elif interest == "compound":
                a = p * math.pow((1+r),t)
                print(f"The amount of interest you'll earn on your home investment is: {a} !")
            else:
                print("You have entered an incorrect value, please try again.")
                continue
                

        elif welcome_message == "bond":
            house_value = int(input("Please enter the present value of the house: "))
            interest_rate = int(input("Please enter the interest rate: "))
            months = int(input("Please enter the number of months you plan to repay the bond: "))
            p = house_value
            i = (interest_rate / 100) / 12 
            n = months
            repayment = round(i * p) / (1 - (1 + i) ** (-n))
            print(f"The amount you will have to pay on a home loan is: {repayment} GBP. ")
        else:
            print("You have entered an incorrect value, please try again.")
        break
            

    except ValueError:
        print("You have entered an incorrect value, please try again. ")
        break


