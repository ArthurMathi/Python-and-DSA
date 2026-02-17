# Student total Fees amount
studentType=input("Enter the Acadmaic Type(Management/Merit): ")
if studentType=="Management":
    studentType2=input("Enter the Student Type(Hosteller/Day Scholar): ")
    if studentType2=="Hosteller":
        tuitionFees=30000
        hostelFees=20000
        totalFees=(tuitionFees+hostelFees)*2.5
        print("The total fees for the student is $",totalFees)
    elif studentType2=="Day Scholar":
        tuitionFees=30000
        BusFees=10000
        totalFees=(tuitionFees+BusFees)*2.5   
        print("The total fees for the student is $",totalFees)
elif studentType=="Merit":
    studentType2=input("Enter the Student Type(Hosteller/Day Scholar): ")
    if studentType2=="Hosteller":
        tuitionFees=30000
        hostelFees=20000
        totalFees=tuitionFees+hostelFees
        print("The total fees for the student is $",totalFees)
    elif studentType2=="Day Scholar":
        tuitionFees=30000
        BusFees=10000
        totalFees=tuitionFees+BusFees   
        print("The total fees for the student is $",totalFees)
