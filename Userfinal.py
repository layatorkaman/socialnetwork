import json
import friends
import myjson
import logging
list_of_users={"ali":{"username":"ali","password":"a","posts":{},"follower":[],"following":[],"profile":None},
               "zahra":{"username":"zahra","password":"b","posts":{},"follower":[],"following":[],"profile":None},
               "hossein":{"username":"hossein","password":"c","posts":{},"follower":[],"following":[],"profile":None}}
list_of_profile={}
class User:
    def __init__(self, username, password,posts=[], follower=[],following=[],profile=None):
        self.username = username
        self.password = password
        self.posts = posts
        self.follower = follower
        self.following = following
        self.profile = profile

    def register(self,check_pass):

         try:
            assert self.password == check_pass
            self.password = check_pass
            new_user = User(self.username, self.password)

            return new_user

         except:
             return 0

    def login(self):
        list_of_users=myjson.load_with_json("new_users.json")
        if self.username in list_of_users.keys():
             if list_of_users[self.username]["password"] == self.password:
                 my_account = User(self.username, self.password)
                 2
                 return my_account
             else:
                 n = 0
                 while n < 2:
                     n += 1
                     pass_again = input("your password was wrong try again:")
                     if list_of_users[self.username]["password"] == pass_again:
                         my_account = User(self.username, pass_again)


                         return my_account

             return 0

        else:
            return 2


    def add_profile(self,new_profile):
        self.profile = new_profile

    def select_profile(self):
        new_profile=friends.Profile.get_info().creat_profile(self.username)

        list_of_profile[esme] = {"first name":self.first_name,"last name":self.last_name,
                                 "tel":self.tel,"email":self.email}
        myjson.dump_in_json("new_users.json",list_of_users[esme])
        return list_of_profile[esme]

    def add_post(self,new_post):
        new_post.post_id=(len(self.posts))+1
        self.posts.append(new_post)

        return new_post


    def add_following(self,myfriend):
        self.following.append(myfriend)
        return self.following

    def add_follower(self,myname):
        self.follower.append(myname)
        return self.follower





    @classmethod
    def get_info(cls):
        username = input("enter your user:")
        password = input("enter your pass:")



        return User(username, password)



    def __str__(self):
        return f' {self.username}' \
               f' {self.password}'\
               f' {self.posts}'\
               f' {self.profile}'\
               f' {self.following}'\
               f' {self.follower}'

