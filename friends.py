from _datetime import datetime
list_of_profile = {}
class Profile:

    def __init__(self,first_name,last_name,tel,email,bio=None):
        self.first_name=first_name
        self.last_name=last_name
        self.tel=tel
        self.email=email
        self.bio=bio




    @classmethod
    def get_info(cls):
        first_name=input("enter your name:")
        last_name=input("enter your last name:")
        tel = int(input("enter your telephone number:"))
        email = input("enter your e_mail:")
        bio = input("what would you like to say about yourself to others:")
        return Profile(first_name,last_name,tel,email,bio)

    def __str__(self):
        return f' {self.first_name}'\
               f' {self.last_name}'\
               f' {self.tel}'\
               f' {self.email}'\
               f' {self.bio}'


list_of_posts={}
class Post:
    def __init__(self, title,text, like=0, comment=0,post_id=0):
        """

        :param post_id:
        :param title:
        :param text:
        :param like:
        :param comment:
        """
        self.post_id=post_id
        self.title=title
        self.text=text
        # self.date_time=datetime.today()
        self.like=like
        self.comment=comment


    def add_post(self,esme):
        new_post = Post(self.title, self.text, self.like, self.comment)
        return new_post


    @classmethod
    def get_info(cls):
        title = input("enter your title :")
        text = input("Enter your text:")
        return Post( title, text)

    def __str__(self):
        return f' {self.title}' \
               f' {self.text}'\
               f' {self.like}'\
               f' {self.comment}'

