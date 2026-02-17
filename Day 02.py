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
AccountBalance=float(input("Enter your current account balance: "))
withdrawalAmount=float(input("Enter the amount you want to withdraw: "))
Transactionlimit=10000
if withdrawalAmount>AccountBalance:
    print("Insufficient funds. Your account balance is $",AccountBalance)
elif withdrawalAmount>Transactionlimit:
    print("Transaction limit exceeded. The maximum withdrawal amount is $",Transactionlimit)
else:
    AccountBalance-=withdrawalAmount
    print("Withdrawal successful. Your new account balance is $",AccountBalance)