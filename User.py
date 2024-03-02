from Observer import *
from Posts import *

class User:
    """
    Represents a user in a social media platform.

    Attributes:
        _userName (str): The username of the user.
        _password (str): The password of the user.
        _is_online (bool): Indicates whether the user is currently online.
        number_of_posts (int): The number of posts made by the user.
        observer (Observer): The observer object for the user.
        publisher (Publisher): The publisher object for the user.
    """

    def __init__(self, username: str, password: str):
        """
        Initializes a User object with the given username and password.

        Parameters:
            username (str): The username of the user.
            password (str): The password of the user.
        """
        self._userName = username
        self._password = password
        self._is_online = True
        self.number_of_posts = 0
        self.observer = Observer(self._userName)
        self.publisher = Publisher(self._userName)

    def get_password(self):
        """
        Get the password of the user.

        Returns:
            str: The password of the user.
        """
        return self._password

    def get_username(self):
        """
        Get the username of the user.

        Returns:
            str: The username of the user.
        """
        return self._userName

    def is_online(self):
        """
        Check if the user is online.

        Returns:
            bool: True if the user is online, False otherwise.
        """
        return self._is_online

    def make_online(self):
        """Set the user's online status to True."""
        self._is_online = True

    def make_offline(self):
        """Set the user's online status to False."""
        self._is_online = False

    def follow(self, user):
        """
        Follow another user.

        Parameters:
            user (User): The user to follow.
        """
        if self.is_online:
            user.publisher.add_observer(self.observer)

    def unfollow(self, user):
        """
        Unfollow another user.

        Parameters:
            user (User): The user to unfollow.
        """
        if self.is_online:
            user.publisher.remove_observer(self.observer)

    def get_followers_amount(self):
        """
        Get the number of followers of the user.

        Returns:
            int: The number of followers.
        """
        return self.publisher.num_followers()

    def publish_post(self, type, name, price="", location=""):
        """
        Publish a post.

        Parameters:
            type (str): The type of the post.
            name (str): The name of the post.
            price (str, optional): The price of the post (default is "").
            location (str, optional): The location of the post (default is "").

        Returns:
            Post: The newly published post.
        """
        if self.is_online():
            new_post = PostFactory.PostCreator(self, type, name, price, location)
            self.number_of_posts = self.number_of_posts + 1
            self.publisher.update_new_post(new_post)
            return new_post

    def print_notifications(self):
        """Print notifications for the user."""
        print(self.observer)

    def __str__(self):
        """
        Return a string representation of the user.

        Returns:
            str: A string representation of the user.
        """
        ans = (f"User name: {self._userName}, Number of posts: {self.number_of_posts}, Number of followers: {self.get_followers_amount()}")
        return ans
