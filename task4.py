"""
Help Jenny keep track of her expenses!
Each month, she needs to keep track of:
1. The current balance on her credit card
2. The total amount of her purchases
3. The total amount that she pays off
4. If she has an unpaid balance, then 2% of the current balance is charged to her

Write a program that asks her to enter in her total purchases as
well as how much she pays off.  Calculate any interest that she must add to her
balance and display her total balance at the end of the month.

A sample for the first few months is shown below:

Enter total purchases for month(1) : 100
Enter total payments for month(1)  : 75
2% interest has been charged: 0.5
Your closing balance is $25.5

Enter total purchases for month(2) : 100
Enter total payments for month(2)  : 75
2% interest has been charged: 1.01
Your closing balance is $51.51

"""


total = 0
for i in range(1):
    x = int(input("enter total purchases for month 1: "))
    y = int(input("enter total payments for month 1: "))

if y <= x:
    num  = x - y
    interest= num * 0.02
    print(f" 2% interest has been charged {interest}")
    balance = num + interest
    print(balance)


for i in range(1):
    x2 = int(input("enter total purchases for month 2: "))
    y2 = int(input("enter total payments for month 2: "))

if (y2 <= x2) + num:
    interest2 = int(interest)
    num2  = x2 - y2
    interest2 = num2 * 0.02
    print(f" 2% interest has been charged {interest}")
    Newbalance = num2 + interest2
    print(Newbalance)






