# mortgage.py
#
# Exercise 1.7
# mortgage.py

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_starth_month = 0
extra_payment_end_month = 12 
extra_payment = 1000 


i = 0 
while principal > 0:
    combined_payment = payment
    if i >= extra_payment_starth_month and i < extra_payment_end_month:
        combined_payment += extra_payment

    principal = principal * (1+rate/12) - combined_payment
    total_paid = total_paid + combined_payment

    # Correct for last month
    if principal < 0:
        total_paid =- principal
        principal = 0

    i += 1

    
    print("Month: " + str(i) + "\tTotal paid: " + str(round(total_paid,2)) + "\tRemaining: " + str(round(principal,2)))

