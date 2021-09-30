# a = 45

# if(a>3):
#     print("The value of a is greater than 3")
# elif(a>7):
#     print("The value of a is greater than 7")    
# else:
#     print("The value is not grater than 3 or 7")

# # In and is 
# in mtlb list me h k nai 
# is mtlb dono ka object ka value same hai

# num1 = int(input("Enter your number 1 :"))
# num2 = int(input("Enter your number 2 :"))
# num3 = int(input("Enter your number 3 :"))
# num4 = int(input("Enter your number 4 :"))

# if(num1 > num4):
#     f1 = num1

# else:
#     f1 = num4 


# if(num2 > num3):
#     f2 = num2

# else:
#     f2 = num3 


# if(f1 > f2):
#     print(str(f1) + "is greatest")
# else:
#     print(str(f2) + "is greatest")


# sub1 =int(input("Enter your first subject marks\n "))
# sub2 =int(input("Enter your second subject marks\n "))
# sub3 =int(input("Enter your third subject marks\n "))

# if (sub1<33 or sub2<3 or sub3<33):
#     print("You are failed because you have less than 33  percent in one of the subjects")
# elif(sub1 + sub2 + sub3)/3 < 40 :
#     print("You are fail due to total percentage less than 40")
# else:
#     print("Congratulations You are passed ")



# a = input("Enter username")

# if (len("a")<10) :
#     print("Your username contains less than 10 characters")
# else:
#     print("Your username contains more than 10 characters ")

# names =["shipra","aditi","rohit","rohan"]
# name =input("Enter your name to check\n")
# if name in names:
#     print("Your name is present name in the list")
# else:
#     print(" Your name is not in the list ")


marks = int(input("Enter your marks"))

if marks >= 90:
    grade = "Ex"
elif marks >= 80:
    grade = "A" 
elif marks >= 70:
    grade = "B" 
elif marks >= 60:
    grade = "C" 
elif marks >= 50:
    grade = "D" 
else:
    grade = "F"

print("Your grade is "+ grade)



