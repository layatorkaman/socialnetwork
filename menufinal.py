import Userfinal
import friends
import myjson
import logging
import time
from hashlib import md5

mylogger = logging.getLogger(__name__)
mylogger.setLevel(logging.INFO)
file_handeler = logging.FileHandler('file.log')
std_handeler = logging.StreamHandler()
file_handeler.setLevel(logging.INFO)
std_handeler.setLevel(logging.INFO)
log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
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
            r = friends.Profile.get_info()
            myname.add_profile(r)
            my_profile = {"first name": r.first_name, "last name": r.last_name, "tel": r.tel, "email": r.email,
                          "bio": r.bio}

            myjson.dump_in_json("new_users.json", my_profile, myname.username, "profile")
            mylogger.info("profile added")
            print(f"your profile was created: my name is"
                  f" {r.first_name + r.last_name} my telephone number is {r.tel} my"
                  f" email is {r.email} and i wand to say another person that:{r.bio} ")
            menu_of_myaccount(myname)

        elif select3 == 2:
            data = myjson.load_with_json("new_users.json")
            try:
                r = data[myname.username]["profile"]
                print(f"my name is {r['first name'] + r['last name']}"
                      f" and my telephone number is {r['tel']} and my Email is {r['email']} and {r['bio']}")
                menu_of_myaccount(myname)
            except KeyError:
                print('you need to make your profile first')
                menu_of_myaccount(myname)

        elif select3 == 3:
            data = myjson.load_with_json("new_users.json")
            data2 = data.keys()
            new_list = []
            for i in data2:
                if i == myname.username:
                    continue
                else:
                    new_list.append(i)
            print(new_list)
            name_of_person = input("who would you like to see her/him profile?\n")
            try:
                data3 = data[name_of_person]["profile"]

                print(f"his or her name is {data3['first name']}  {data3['last name']}"
                      f" and  telephone number is {data3['tel']} and  Email is {data3['email']} and "
                      f" she or he saied about him or her{data3['bio']}")

            except KeyError:
                print(f"{name_of_person} has not defined profile ")
            menu_of_myaccount(myname)

    elif select2 == 2:
        print("what do you do?\n")
        select4 = int(input("1.add  new post\n"
                            "2.edit  one post\n"
                            "3.delete one post\n"
                            "4.show my posts\n"
                            "5.show posts's another person\n"
                            "6.Back"))
        if select4 == 1:
            data = myjson.load_with_json("new_users.json")
            d2 = data[myname.username]["number of post"]
            d2 += 1
            r = friends.Post.get_info()
            t = myname.add_post(r, d2)
            my_post = {"title": t.title, "text": t.text,
                       "date": t.post_time.strftime("%Y-%m-%d %H:%M:%S"),
                       "comment": t.comment, "like": t.like}

            myjson.dump_in_json("new_posts.json", my_post, myname.username, myname.number_of_post)
            mylogger.info("new post added")
            print(f"you have a new post")
            data2 = myname.number_of_post
            myjson.dump_in_json("new_users.json", data2, myname.username, "number of post")
            menu_of_myaccount(myname)

        elif select4 == 2:
            data = myjson.load_with_json("new_posts.json")
            data1 = data[myname.username]
            for key, post in data1.items():
                print(f"{key} ==>{post['title']}")
            select_post = input("please enter number of post would you like to edit ? ")
            print(friends.edit_post(myname.username, select_post))
            menu_of_myaccount(myname)

        elif select4 == 3:
            data = myjson.load_with_json("new_posts.json")
            data1 = data[myname.username]
            for key, post in data1.items():
                print(f"{key} ==>{post['title']}")
            select_post = input("please enter number of post would you like to delete ? ")
            print(friends.delete_post(myname.username, select_post))
            menu_of_myaccount(myname)

        elif select4 == 4:
            data = myjson.load_with_json("new_posts.json")
            r = data[myname.username]
            t = r.values()
            for i in t:
                print(f"{i['title']} : {i['text']} ")
            menu_of_myaccount(myname)

        elif select4 == 5:
            data = myjson.load_with_json("new_posts.json")
            data = data.keys()
            for person in data:
                if person == myname.username:
                    pass
                else:
                    print(person)
            new_person = input("who would you like to see posts:")
            data = myjson.load_with_json("new_posts.json")
            data1 = data[new_person]
            for key, post in data1.items():
                print(f"{key} ==>{post['title']}")
            select_post = input("please enter number of post would you like to see ? ")
            post_show = friends.Post(*(data1[select_post].values()))
            print(post_show)
            add_like = int(input("would you like to add a LIKE ? 1:yes 2:No"))
            if add_like == 1:
                print(friends.adding_like(new_person, select_post))

            else:
                pass
            answer = int(input("do you want submit a comment?:1.Yes 2.No"))
            if answer == 1:
                new_comment = friends.Comment.get_info(myname)
                print(friends.writing_comment(new_person, select_post, new_comment))
                mylogger.info("new comment added")

            else:
                pass
            menu_of_myaccount(myname)

        elif select4 == 6:
            menu_of_myaccount(myname)
        else:
            print("your input is invalid")

    elif select2 == 3:
        select5 = int(input("1.add new friend\n"
                            " 2.show my following\n "
                            "3.show my follower\n"
                            "4.Back"))
        if select5 == 1:
            question1 = input("do you know her or him Id?y/n:")
            if question1 == "N" or question1 == "n":

                data = myjson.load_with_json("new_users.json")
                new = []
                for i in data:
                    if i == myname.username:
                        continue
                    else:
                        new.append(i)
                print(new)
                question2 = input("who would you like to add her/him to your friends?\n")

            elif question1 == "Y" or question1 == "y":
                question2 = input("enter her or him Id:")
            r = myname.add_following(question2)
            myjson.dump_in_json("new_users.json", r, myname.username, "following")
            mylogger.info("new friend added")
            print(f"{question2} added to {myname.username} following list ")
            data = myjson.load_with_json("new_users.json")
            t = data[question2]
            if "follower" in t.keys():
                data[question2]["follower"].append(myname.username)
                myjson.dump_in_json("new_users.json", data[question2], question2)
            else:
                myjson.dump_in_json("new_users.json", [myname.username], question2, "follower")

        elif select5 == 2:
            data = myjson.load_with_json("new_users.json")
            try:
                print(data[myname.username]["following"])
            except KeyError:
                print("you have not got any following")
            menu_of_myaccount(myname)

        elif select5 == 3:
            data = myjson.load_with_json("new_users.json")
            try:
                print(data[myname.username]["follower"])
            except KeyError:
                print("you have not got any follower")
            menu_of_myaccount(myname)

        elif select5 == 4:
            menu_of_myaccount(myname)

    elif select2 == 4:
        first_menu()

    else:
        print("YOUR INPUT INVALID")
        first_menu()


def first_menu():
    print("************************************* welcome to first step: *********************************************")
    try:
        select = int(input("1.Register\n"
                           "2.log in\n"
                           "3.Exit\n"))

        if select == 1:

            back = Userfinal.User.get_info()
            data = myjson.load_with_json("new_users.json")
            if back.username in data.keys():
                print("sorry this account created already")
                first_menu()
            else:
                check_pass = input("enter check password:")
                back2 = back.register(check_pass)
                if back2 != 0:
                    password2 = str(back2.password).encode()
                    hashed_password = md5(password2).hexdigest()

                    data = {"username": back2.username, "password": hashed_password, "number of post": 0}

                    myjson.dump_in_json("new_users.json", data, back2.username)
                    mylogger.info('created account')

                    print(f"{back2.username} your account created successfully")
                    first_menu()
                elif back2 == 0:
                    print("your password is wrong try again")
                    first_menu()

        elif select == 2:
            back2 = Userfinal.User.get_info()
            t = back2.login()
            if t == 0:
                mylogger.error("ERROR", exc_info=True)
                print("sorry your account deactivate for 5 minutes")
                seconds = 0
                while seconds != 100:
                    time.sleep(1)
                    seconds += 1
                print("you can try again")

            elif isinstance(t, Userfinal.User):
                mylogger.info("log in")
                menu_of_myaccount(t)
                print("welcome to your account")

            elif t == 2:
                print("this account not exist")

        elif select == 3:
            pass

        else:
            print("your input invalid")

    except ValueError:
        print("your input is invalid ")
        first_menu()


first_menu()
