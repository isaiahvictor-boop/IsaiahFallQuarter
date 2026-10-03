numberGrade = int(input("enter your grade"))

if(numberGrade >= 90):
    print("you got an A, great job!")
elif(80 <= numberGrade <= 89):
    print("you got an B, great job!")
elif(70 <= numberGrade <= 79):
    print("you got an C, great job!")
elif(60 <= numberGrade <= 69):
    print("you got an D, great job!")
else:
    print("you got an F, Boo!")