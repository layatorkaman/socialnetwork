import csv
import classes
while True:
    select1 = int(input("please select : 1-register 2-log in  "))
    if select1 == 1:
        new_user = classes.User.get_info()
        print(new_user.register())
    elif select1 == 2:
        my_user = classes.User.get_info()

        n = 0
        while n < 3:
            check = my_user.login()
            if  check== 2:
                n += 1
                print("your password is wrong")
                pass_again = input("enter password again")
                my_user = classes.User(my_user.username, pass_again)
                my_user.login()

            elif check ==1 :

                print("welcome")
                break

            elif n == 2 and  check==2:
                print("your account was inactive for 1 hour ")
                break
            elif check==3:
                print("ok")
            else:
                print("exit the page")

        select2 = int(input("what do you do? 1-show my profile 2-show my post 3-show all users "
                            "4-show another person,s posts"))
        if select2 == 1:
            print("show my profile with call class profile")