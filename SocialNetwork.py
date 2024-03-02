from User import *


class SocialNetwork:
    _instance = None

    def __new__(cls, networkName):
        if cls._instance is None:
            cls._instance = super(SocialNetwork, cls).__new__(cls)
            cls._instance.usersExist = []
            cls._instance.theNetworkName = networkName
            print(f"The social network {cls._instance.theNetworkName} was created!")
        return cls._instance

    def sign_up(self, username, password):
        flag = True
        for user in self.usersExist:
            if user == username:
                flag = False

        if len(password) < 4 or len(password) > 8:
            flag = False

        if flag:
            new_user = User(username, password)
            self.usersExist.append(new_user)
            return new_user

    def log_in(self, username, password):
        user = self.get_user(username)
        if (user is not None) and user.get_password() == password:
            user.make_online()
            print(f"{username} connected")

    def log_out(self, username):
        user = self.get_user(username)
        if user is not None and user.is_online():
            user.make_offline()
            print(f"{username} disconnected")

    def get_user(self, username):
        for user in self.usersExist:
            if user.get_username() == username:
                return user
        return None

    def __str__(self):
        ans = f"{self.theNetworkName} social network:\n"
        for user in self.usersExist:
            ans += user.__str__() + "\n"
        return ans
