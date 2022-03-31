usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "poramet" and passwordInput == "123" :
    print("loginComplete")
    print("1.Apple price = 12 THB")
    print("2.Mango price = 15 THB")
    userselected = int(input("What are you want to select ? : "))
    if userselected == 1:
        num1 = int(input("How many apples do you want ? : "))
        print("Total Apple price = ",num1*12,"THB")
    elif userselected == 2:
        num2 = int(input("How many mangoes do you want ? : "))
        print("Total mango price = ",num2*15,"THB")
else:
    print("loginFail")
print("Thank You ><")