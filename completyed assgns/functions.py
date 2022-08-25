def highestnum(num1,num2=30,num3=50):
    if (num1 > num2) and (num1 > num3):
        return num1
    elif (num2 > num3):
        return num2
    else:
        return num3
var = highestnum(10,50,90)
print(var,"highest")