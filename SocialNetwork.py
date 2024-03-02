from User import *


class SocialNetwork:
    """
    A class representing a social network.

    This class implements the Singleton design pattern, ensuring that only one instance
    of the social network can exist.

    Attributes:
        _instance (SocialNetwork): An instance of the SocialNetwork class.
        usersExist (list): A list of existing users in the social network.
        theNetworkName (str): The name of the social network.
    """

    _instance = None

    def __new__(cls, networkName):
        """
        Creates a new instance of the SocialNetwork class if it doesn't already exist.

        Args:
            networkName (str): The name of the social network.

        Returns:
            SocialNetwork: An instance of the SocialNetwork class.
        """
        if cls._instance is None:
            cls._instance = super(SocialNetwork, cls).__new__(cls)
            cls._instance.usersExist = []
            cls._instance.theNetworkName = networkName
            print(f"The social network {cls._instance.theNetworkName} was created!")
        return cls._instance

    def sign_up(self, username, password):
        """
        Registers a new user in the social network.

        Args:
            username (str): The username of the new user.
            password (str): The password of the new user.

        Returns:
            User: The newly created User object if successful, None otherwise.
        """
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
        """
        Logs in a user to the social network.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        """
        user = self.get_user(username)
        if (user is not None) and user.get_password() == password:
            user.make_online()
            print(f"{username} connected")

    def log_out(self, username):
        """
        Logs out a user from the social network.

        Args:
            username (str): The username of the user.
        """
        user = self.get_user(username)
        if user is not None and user.is_online():
            user.make_offline()
            print(f"{username} disconnected")

    def get_user(self, username):
        """
        Retrieves a user from the social network by username.

        Args:
            username (str): The username of the user to retrieve.

        Returns:
            User: The User object if found, None otherwise.
        """
        for user in self.usersExist:
            if user.get_username() == username:
                return user
        return None

    def __str__(self):
        """
        Returns a string representation of the SocialNetwork object.

        Returns:
            str: A string representing the social network and its users.
        """
        ans = f"{self.theNetworkName} social network:\n"
        for user in self.usersExist:
            ans += user.__str__() + "\n"
        return ans
