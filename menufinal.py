import Userfinal
import friends
import myjson
import logging

mylogger=logging.getLogger(__name__)
mylogger.setLevel(logging.INFO)
file_handeler=logging.FileHandler('file.log')
std_handeler=logging.StreamHandler()
file_handeler.setLevel(logging.INFO)
std_handeler.setLevel(logging.INFO)
log_format= logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handeler.setFormatter(log_format)
std_handeler.setFormatter(log_format)
mylogger.addHandler(file_handeler)
mylogger.addHandler(std_handeler)


def menu_of_myaccount(myname):
    print(f"*************************************  welcome {myname.username} *************************************:")
    select2 = int(input("1.Profile\n"
                         "2.Post\n"
                         "3.Friends\n"
                         "4.Back"))
    if select2 == 1:
        print("what do you do?\n")
        select3 = int(input("1.create or edit my profile\n"
                            "2.show my profile\n"
                            "3.show profile another person\n"
                            "4.Back"))
        if select3 == 1:
             r=friends.Profile.get_info()
             myname.add_profile(r)
             my_profile={"first name":r.first_name,"last name":r.last_name,"tel":r.tel,"email":r.email,"bio":r.bio}

             myjson.dump_in_json("new_users.json",my_profile,myname.username,"profile")
             mylogger.info("profile added")
             print(f"your profile was created: my name is"
                   f" {r.first_name + r.last_name } my telephone number is {r.tel} my"
                   f" email is {r.email} and i wand to say another person that:{r.bio} ")
             menu_of_myaccount(myname)



        elif select3 == 2:
            data=myjson.load_with_json("new_users.json")
            r=data[myname.username]["profile"]

            print(f"my name is { r['first name'] +  r['last name'] }"
                   f" and my telephone number is {r['tel']} and my Email is {r['email']} and {r['bio']}")
            menu_of_myaccount(myname)

        elif select3 == 3:
            data = myjson.load_with_json("new_users.json")
            data2=data.keys()
            new_list = []
            for i in data2:
                 if i == myname.username:
                     continue
                 else:
                     new_list.append(i)
            print(new_list)
            name_of_person = input("who would you like to see her/him profile?\n")
            data3=data[name_of_person]["profile"]
            print(f"his or her name is { data3['first name']}  {data3['last name']}"
                  f" and  telephone number is {data3['tel']} and  Email is {data3['email']} and "
                  f" she or he saied about him or her{data3['bio']}")
            menu_of_myaccount(myname)

    elif select2 == 2:
        print("what do you do?\n")
        select4 = int(input("1.add  new post\n"
                            "2.edit  new post\n"
                            "3.show my posts\n"
                            "4.show posts's another person\n"
                            "5.Back"))
        if select4 == 1:
            r = friends.Post.get_info()
            t=myname.add_post(r)
            my_post =  {"title": t.title, "text": t.text, "comment":t.comment,"like":t.like}

            myjson.dump_in_json("new_posts.json", my_post, myname.username,t.post_id)
            mylogger.info("new post added")
            print(f"you have a new post")
            menu_of_myaccount(myname)

        elif select4 ==2:
            pass
      
        elif select4 == 3:
            data = myjson.load_with_json("new_posts.json")
            r = data[myname.username]
            t=r.values()
            for i in t:
                print(f"{i['title']} : {i['text']}")

            menu_of_myaccount(myname)

        elif select4 == 4:
            data=myjson.load_with_json("new_users.json")
            t=data.keys()
            for i in t:
                print(i)
            new_person=input("how would you like to see posts:")
            data=myjson.load_with_json("new_posts.json")

            data1=data[new_person]
            data2=data1.values()
            for i in data2:
                print(f"the title is {i['title']} and the text is {i['text']} "
                      f"and like is {i['like']} and comment {i['comment']}")

            menu_of_myaccount(myname)


        elif select4 == 5:
            menu_of_myaccount(myname)
        else:
            print("your input is invalid")

    elif select2 == 3:
        select5=int(input("1.add new friend\n"
                          " 2.show my following\n "
                          "3.show my follower\n"
                          "4.Back"))
        if select5 == 1:
            questtion1=input("do you know her or him Id?y/n:")
            if questtion1 == "N" or questtion1 == "n":

                data=myjson.load_with_json("new_users.json")
                new = []
                for i in data:
                    if i == myname.username:
                        continue
                    else:
                        new.append(i)
                print(new)
                questtion2 = input("who would you like to add her/him to your friends?\n")

            elif questtion1 == "Y" or questtion1 == "y":
                questtion2=input("enter her or him Id:")
            r = myname.add_following(questtion2)
            myjson.dump_in_json("new_users.json",r,myname.username,"following")
            mylogger.info("new friend added")
            print(f"{questtion2} added to {myname.username} followering list ")
            data=myjson.load_with_json("new_users.json")
            t=data[questtion2]
            if "follower" in t.keys():
                data[questtion2]["follower"].append(myname.username)
                myjson.dump_in_json("new_users.json",data[questtion2],questtion2)
            else:
                myjson.dump_in_json("new_users.json",[myname.username],questtion2,"follower")



        elif select5 == 2:
            data=myjson.load_with_json("new_users.json")
            print(data[myname.username]["following"])
            menu_of_myaccount(myname)

        elif select5 == 3:
            data = myjson.load_with_json("new_users.json")
            print(data[myname.username]["follower"])
            menu_of_myaccount(myname)

        elif select5 == 4:
            menu_of_myaccount(myname)


while True:
    print("*************************************welcome to first step:*********************************************")

    select = int(input("1.Register\n"
               "2.log in\n"
               "3.Exit\n"))
    if select == 1:

        back = Userfinal.User.get_info()
        check_pass = input("enter check password:")
        back2=back.register(check_pass)
        if back2 != 0:
            data={"username":back2.username,"password":back2.password}

            myjson.dump_in_json("new_users.json",data,back2.username)
            mylogger.info('created account')

            print(f"{back2.username} your account created succesfully")
        elif back2 ==0:
            print("your password is wrong try again")



    elif select == 2:
        back2 = Userfinal.User.get_info()
        t = back2.login()
        if t == 0:
            mylogger.error("ERROR" , exc_info=True)
            print("sorry your account deactive for 1 houre")
        elif isinstance(t, Userfinal.User):
            mylogger.info("log in" )
            menu_of_myaccount(t)
            print("welcome to your account")

            break
        elif t == 2:
            print("this account not exist")

    elif select == 3:
        break
    else:
        print("your input invalid")


