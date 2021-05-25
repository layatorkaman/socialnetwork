from datetime import datetime
import myjson


class Profile:

    def __init__(self, first_name, last_name, tel, email, bio=None):
        self.first_name = first_name
        self.last_name = last_name
        self.tel = tel
        self.email = email
        self.bio = bio

    @classmethod
    def get_info(cls):
        first_name = input("enter your name:")
        last_name = input("enter your last name:")
        tel = int(input("enter your telephone number:"))
        email = input("enter your e_mail:")
        bio = input("what would you like to say about yourself to others:")
        return Profile(first_name, last_name, tel, email, bio)

    def __str__(self):
        return f' {self.first_name}' \
               f' {self.last_name}' \
               f' {self.tel}' \
               f' {self.email}' \
               f' {self.bio}'


class Post:
    def __init__(self, title, text, post_time, comment=[], like=0):
        """

        :param post_id:number uniq for each post
        :param title: title for post
        :param text: text for post
        :param like: number of like
        :param comment: comment for each post
        """
        self.title = title
        self.text = text
        self.post_time = datetime.strptime(post_time, "%Y-%m-%d %H:%M:%S")
        self.like = like
        self.comment = comment

    def add_post(self, esme):
        new_post = Post(self.title, self.text, self.post_time, self.like, self.comment)
        return new_post

    def add_comment(self, new_comment):
        self.comment.append(new_comment)
        return new_comment

    @classmethod
    def get_info(cls):
        title = input("enter your title :")
        text = input("Enter your text:")
        post_time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

        return Post(title, text, post_time)

    def __str__(self):
        return f'title:{self.title}\n post time: {self.post_time}\n' \
               f'text:{self.text} \n  likes:{self.like} comment:{len(self.comment)} '


class Comment:
    def __init__(self, writer, text, comment_time):
        """
        :param writer: person who write comment
        :param text: the text
        :param post_time: the time which comment submit
        """
        self.writer = writer
        self.text = text
        self.comment_time = datetime.strptime(comment_time, "%Y-%m-%d %H:%M:%S")

    @classmethod
    def get_info(cls, myname):
        writer = myname.username
        text = input("Enter comment:")
        comment_time = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
        new_comment = Comment(writer, text, comment_time)
        return new_comment

    def __str__(self):
        return f' {self.writer}' \
               f' {self.text}' \
               f' {self.comment_time}'


def writing_comment(select_name, select_post, my_comment):
    my_comment = {"writer": my_comment.writer, "comment": my_comment.text,
                  "comment time": my_comment.comment_time.strftime("%Y-%m-%d %H:%M:%S")}
    data = myjson.load_with_json("new_posts.json")
    data2 = data[select_name][select_post]
    data2["comment"].append(my_comment)
    myjson.dump_in_json("new_posts.json", data2, select_name, select_post)
    return "comment added"


def adding_like(select_name, select_post):
    data = myjson.load_with_json("new_posts.json")
    data2 = data[select_name][select_post]
    data2["like"] += 1
    myjson.dump_in_json("new_posts.json", data2, select_name, select_post)
    return "LIKE submit"


def delete_post(name, select_post):
    data = myjson.load_with_json("new_posts.json")
    print(data[name][select_post])
    are_you_sure = int(input("Are you sure want delete your post? 1:yes 2:No"))
    if are_you_sure == 1:
        data[name].pop(select_post)
        myjson.dump_in_json("new_posts.json", data[name], name)
        return " your post deleted"
    else:
        pass


def edit_post(name, select_post):
    data = myjson.load_with_json("new_posts.json")
    new_data = data[name][select_post]
    print(new_data)
    select_edit = int(input("which one would you like to edit: 1.title 2.Text"))
    if select_edit == 1:
        new_data["title"] = input("enter new title")

    elif select_edit == 2:
        new_data["text"] = input("enter new post")
    myjson.dump_in_json("new_posts.json", new_data, name, select_post)
    return "your post edited"
