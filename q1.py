#Charles Dunlow
# A credit card company computes a customer's "minimum payment" according to the following rule. The minimum payment is equal to either $10 or 2.1% of the customer's balance, whichever is greater; however, if a $10 minimum payment exceeds the balance, then the minimum payment is the balance. Write a program to return the minimum payment. Assume that the variable balance contains the customer's balance.
#   Example 1: if your balance is 1000, then your program should return 21. 
#   Example 2: if your balance is 600, then your program should return 12.6. 
#   Example 3: if your balance is 25, then your program should return 10. 
#   Example 4: if your balance is 8, then your program should return 8. 

def computeMinimumPayment( balance ):
    #TODO write code inside this function that achieves the functionality described above
    if .021 * balance > 10:     #finds if the payment is larger than 10
        minimumPay = .021 * balance; #if it is larger than it calculates the min payment
    else:
        minimumPay = 10   #if balance equals 10 the min pay is 10

    if minimumPay > balance:   #if min is larger than balance
        minimumPay = balance;  #min pay equals the balance

    return round(minimumPay,1)
