from Observer import *
from Posts import *


class User:

    def __init__(self, username: str, password: str):
        self._userName = username
        self._password = password
        self._is_online = True
        self.number_of_posts = 0
        self.observer = Observer(self._userName)
        self.publisher = Publisher(self._userName)

    def get_password(self):
        return self._password
    def get_username(self):
        return self._userName

    def is_online(self):
        return self._is_online

    def make_online(self):
        self._is_online = True

    def make_offline(self):
        self._is_online = False

    def follow(self, user):
        if self.is_online:
            user.publisher.add_observer(self.observer)

    def unfollow(self, user):
        if self.is_online:
            user.publisher.remove_observer(self.observer)

    def get_followers_amount(self):
        return self.publisher.num_followers()

    def publish_post(self, type, name, price="", location=""):
        if self.is_online():
            new_post = PostFactory.PostCreator(self, type, name, price, location)
            self.number_of_posts = self.number_of_posts + 1
            self.publisher.update_new_post(new_post)
            return new_post

    def print_notifications(self):
        print(self.observer)

    def __str__(self):

        ans = (f"User name: {self._userName}, Number of posts: {self.number_of_posts}, Number of followers: {self.get_followers_amount()}")
        return ans