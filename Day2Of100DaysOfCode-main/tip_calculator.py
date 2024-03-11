# A function that calculates the tip of a bill after a meal

def tipping_system():
    print("Welcome to our tipping system!")
    bill_total = int(input("What was the total of this bill?: "))
    tip_percent = int(input("How much would you like to tip?: "))
    bill_split = int(input("How many people is this bill split amongst?: "))
    bill = bill_total * tip_percent/100 
    bill_sum = bill + bill_total
    bill_pp = bill_sum / bill_split
    bill_pp = round(bill_pp, 2)
    
    print(f"Your bill for today is R{bill_pp} per person. Thank you!")
    

tipping_system()
    
