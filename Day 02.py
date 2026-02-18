# # Student total Fees amount
# studentType=input("Enter the Acadmaic Type(Management/Merit): ")
# if studentType=="Management":
#     studentType2=input("Enter the Student Type(Hosteller/Day Scholar): ")
#     if studentType2=="Hosteller":
#         tuitionFees=30000
#         hostelFees=20000
#         totalFees=(tuitionFees+hostelFees)*2.5
#         print("The total fees for the student is $",totalFees)
#     elif studentType2=="Day Scholar":
#         tuitionFees=30000
#         BusFees=10000
#         totalFees=(tuitionFees+BusFees)*2.5   
#         print("The total fees for the student is $",totalFees)
# elif studentType=="Merit":
#     studentType2=input("Enter the Student Type(Hosteller/Day Scholar): ")
#     if studentType2=="Hosteller":
#         tuitionFees=30000
#         hostelFees=20000
#         totalFees=tuitionFees+hostelFees
#         print("The total fees for the student is $",totalFees)
#     elif studentType2=="Day Scholar":
#         tuitionFees=30000
#         BusFees=10000
#         totalFees=tuitionFees+BusFees   
#         print("The total fees for the student is $",totalFees)

# ATM cash withdrawal
# AccountBalance=float(input("Enter your current account balance: "))
# withdrawalAmount=float(input("Enter the amount you want to withdraw: "))
# Transactionlimit=10000
# if withdrawalAmount>AccountBalance:
#     print("Insufficient funds. Your account balance is $",AccountBalance)
# elif withdrawalAmount>Transactionlimit:
#     print("Transaction limit exceeded. The maximum withdrawal amount is $",Transactionlimit)
# else:
#     AccountBalance-=withdrawalAmount
#     print("Withdrawal successful. Your new account balance is $",AccountBalance)

# ATM password Based Money Transfer
# AccountBalance=10000
# AccountPassword="1982"
# inputPassword=input("Enter your account password: ")
# if inputPassword==AccountPassword:
#     transferAmount=float(input("Enter the amount you want to withdraw: "))
#     if transferAmount<=0:
#         print("Invalid amount. Withdrawal amount must be greater than zero.")
#     elif transferAmount>AccountBalance:
#         print("Insufficient funds. Your account balance is $",AccountBalance)
#     else:
#         AccountBalance-=transferAmount
#         print("Withdrawal successful. Your new account balance is $",AccountBalance)
# else:
#     print("Incorrect password. Please try again.")

# Movie ticket amount assighing based on Age
# Age = int(input("Enter your age: "))
# showTime = input("Enter show time (Morning/Evening): ")

# if Age < 5:
#     ticketPrice = 0
#     print("You are eligible for a free ticket.")
# elif Age >= 5 and Age <= 17:
#     ticketPrice = 100
#     print("You are eligible for a child ticket.")
# elif Age > 60:
#     ticketPrice = 200
#     print("You are eligible for a senior citizen ticket.")
# else:
#     ticketPrice = 250
#     print("You are eligible for an adult ticket.")

# if showTime == "Morning":
#     if Age > 60:
#         DiscountPrice = (ticketPrice * 0.7)-50
#         print(f"Morning show- 30% senior citizen discount and 50$ discount applied. Your ticket price is ${DiscountPrice}")
#     else:
#         DiscountPrice = ticketPrice - 50
#         print(f"Morning show- 50$ discount applied. Your ticket price is ${DiscountPrice}")
# elif showTime == "Evening":
#     if Age > 60:
#         DiscountPrice = ticketPrice * 0.7
#         print(f"Evening show- 30% senior citizen discount applied. Your ticket price is ${DiscountPrice}")
#     else:
#         print(f"Evening show. Your ticket price is ${ticketPrice}")

  
# print odd number till 100 and sum of odd numbers
# oddNumbers=0
# for i in range(1, 101, 2):
#     print(i)
#     oddNumbers += i
# print("The sum of odd numbers till 100 is:", oddNumbers)

# print even numbers till 100 and sum of even numbers
# evenNumbers=0
# for i in range(0, 101, 2):
#     print(i)
#     evenNumbers += i
# print("The sum of even numbers till 100 is:", evenNumbers)

# 5 mathematical tables
# for i in range(1, 21):
#     print(f"5 x {i} = {5 * i}")

# subject marks average
# totalMarks = 0
# for i in range(1, 6):
#     marks = float(input(f"Enter marks for subject {i}: "))
#     totalMarks += marks
# averageMarks = totalMarks / 5
# print("The average marks for the 5 subjects is:", averageMarks)

# print star pattern
# for i in range(1, 6):
#     print("*" * i)

# for i in range(5,0,-1):
#     print("*"*i)

# print odd number and that sum using while loop 
# oddNumbers=0
# i=1
# while i<=100:
#     print(i)
#     oddNumbers += i
#     i += 2
# print("The sum of odd numbers till 100 is:", oddNumbers)


# print Even number And that sum Using While loop 
# EvenNumber=0
# i=0
# while i<=101:
#     print(i)
#     EvenNumber += i
#     i += 2
# print("The sum of Even number Till 100 is :",EvenNumber)    

# 5th table using While loop
# i=1
# while i<=20:
#     print(f"5 x {i} = {5 * i}")
#     i += 1    

# subject marks average using while loop
# totalMarks = 0
# i = 1
# while i <= 5:
#     marks = float(input(f"Enter marks for subject {i}: "))
#     totalMarks += marks
#     i += 1
# averageMarks = totalMarks / 5
# print("The average marks for the 5 subjects is:", averageMarks)

# star pattern
# i=1
# while i<=5:
#     print("*"*i)
#     i += 1

# i=5
# while i>0:
#     print("*"*i)
#     i -= 1    

# Bus ticket booking resul with name of passenger  
# TotalSeats=10
# SeatNumber=1
# while TotalSeats>0:
#     passengerName=input("Enter the name of the passenger: ")
#     print(f"Bus ticket booked successfully for {passengerName}. Seat Number: {SeatNumber}")
#     TotalSeats -= 1
#     SeatNumber += 1
#     print(f"Remaining seats: {TotalSeats}")
# print("All seats are booked. No more tickets available.")


