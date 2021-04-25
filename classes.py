import csv


class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def register(self):
        check_pass = input("enter check password:")
        try:
            assert self.password == check_pass
            self.password = check_pass
            with open('logininfo.csv', 'a', newline="") as user_data:
                csv_writer = csv.writer(user_data)
                csv_writer.writerow([self.username, self.password])
                return f'{User(self.username, self.password)}your account created'

        except AssertionError:
            return "your password is wrong"

    def login(self):

        with open('logininfo.csv', 'r') as user_data:
            csv_reader = csv.reader(user_data)
            user_pass = {row[0]: row[1] for row in csv_reader}
            if self.username in user_pass.keys():
                if self.password == user_pass[self.username]:
                    return 1
                else:
                    return 2
            else:
                answer = int(input("would you like to creat account:1.yes 2.no"))
                if answer == 1:
                    self.register()
                    return 3
                elif answer == 2:
                    return 2
                else:
                    return "Invalid input"

    @classmethod
    def get_info(cls):
        username = input("enter your user:")
        password = input("enter your pass:")
        return User(username, password)

    def __str__(self):
        return f' {self.username}' \
               f' {self.password}'


class Profile(User):
    def __init__(self, username, password, phone, email, bio=None):
        super().__init__(username, password)
        self.phone = phone
        self.email = email
        self.bio = bio


class Posts:
    def __init__(self, text, date, time):
        self.text = text
        self.date = date
        self.time = time
