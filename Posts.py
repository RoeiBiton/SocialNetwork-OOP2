import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from User import *


class Posts:
    """
    Represents a post made by a user.

    Attributes:
        author (User): The author of the post.
    """

    def __init__(self, author):
        """
        Initializes a Posts object with the given author.

        Parameters:
            author (User): The author of the post.
        """
        self.author = author

    def like(self, user):
        """
        Like the post.

        Parameters:
            user (User): The user who is liking the post.
        """
        if user.is_online:
            user.observer.like_post(self.author.observer)

    def comment(self, user, text):
        """
        Comment on the post.

        Parameters:
            user (User): The user who is commenting on the post.
            text (str): The comment text.
        """
        if user.is_online:
            user.observer.comment_post(self.author.observer, text)


class PostFactory:
    """
    A factory class for creating different types of posts.
    """

    @staticmethod
    def PostCreator(author, type, name, price="", location=""):
        """
        Create a post based on the type.

        Parameters:
            author (User): The author of the post.
            type (str): The type of the post.
            name (str): The name/title of the post.
            price (str, optional): The price (for Sale posts) (default is "").
            location (str, optional): The location (for Sale posts) (default is "").

        Returns:
            Posts: The created post object.
        """
        if type == "Text":
            return TextPost(author, name)
        elif type == "Image":
            return ImagePost(author, name)
        elif type == "Sale":
            return SalePost(author, name, price, location)


class TextPost(Posts):
    """
    Represents a text post.

    Attributes:
        text (str): The content of the text post.
    """

    def __init__(self, author, text):
        """
        Initializes a TextPost object with the given author and text.

        Parameters:
            author (User): The author of the post.
            text (str): The content of the text post.
        """
        super().__init__(author)
        self.username = self.author._userName
        self.text = text

    def __str__(self):
        """
        Return a string representation of the text post.

        Returns:
            str: A string representation of the text post.
        """
        ans = f"{self.username} published a post:\n\"{self.text}\"\n"
        return ans


class ImagePost(Posts):
    """
    Represents an image post.

    Attributes:
        image (str): The path to the image file.
    """

    def __init__(self, author, image):
        """
        Initializes an ImagePost object with the given author and image.

        Parameters:
            author (User): The author of the post.
            image (str): The path to the image file.
        """
        super().__init__(author)
        self.image = image
        self.username = self.author._userName

    def display(self):
        """Display the image."""
        img = mpimg.imread(self.image)
        plt.imshow(img)
        plt.show()
        print("Shows picture")

    def __str__(self):
        """
        Return a string representation of the image post.

        Returns:
            str: A string representation of the image post.
        """
        return f"{self.username} posted a picture\n"


class SalePost(Posts):
    """
    Represents a sale post.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        location (str): The pickup location of the product.
        is_sold (bool): Indicates whether the product is sold.
    """

    def __init__(self, author, name, price, location):
        """
        Initializes a SalePost object with the given author, name, price, and location.

        Parameters:
            author (User): The author of the post.
            name (str): The name of the product.
            price (float): The price of the product.
            location (str): The pickup location of the product.
        """
        super().__init__(author)
        self.username = author._userName
        self.name = name
        self.price = price
        self.location = location
        self.is_sold = False

    def discount(self, percentage, password):
        """
        Apply a discount to the product price.

        Parameters:
            percentage (float): The discount percentage.
            password (str): The author's password for authentication.
        """
        if password == self.author.get_password() and self.author.is_online():
            self.price = self.price * (1 - percentage / 100)
            print(f"Discount on {self.username} product! the new price is: {self.price}")

    def sold(self, password):
        """
        Mark the product as sold.

        Parameters:
            password (str): The author's password for authentication.
        """
        if password == self.author.get_password() and not self.is_sold and self.author.is_online():
            self.is_sold = True
            print(f"{self.username}'s product is sold")

    def __str__(self):
        """
        Return a string representation of the sale post.

        Returns:
            str: A string representation of the sale post.
        """
        if self.is_sold:
            return f"{self.username} posted a product for sale:\nSold! {self.name}, price: {self.price}, pickup from: {self.location}\n"
        else:
            return f"{self.username} posted a product for sale:\nFor sale! {self.name}, price: {self.price}, pickup from: {self.location}\n"
