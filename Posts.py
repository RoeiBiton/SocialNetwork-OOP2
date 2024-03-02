import matplotlib.pyplot as plt
import matplotlib.image as mpimg
class Posts:
    def __init__(self, author):
        self.author = author

    def like(self, user):
        if user.is_online:
            user.observer.like_post(self.author.observer)

    def comment(self, user, text):
        if user.is_online:
            user.observer.comment_post(self.author.observer, text)


class PostFactory:

    @staticmethod
    def PostCreator(author, type, name, price="", location=""):
        if type == "Text":
            return TextPost(author,name)
        elif type == "Image":
            return ImagePost(author, name)
        elif type == "Sale":
            return SalePost(author, name, price, location)


class TextPost(Posts):
    def __init__(self, author, text):
        super().__init__(author)
        self.username = self.author._userName
        self.text = text


    def __str__(self):
        ans = f"{self.username} published a post:\n\"{self.text}\"\n"
        return ans

class ImagePost(Posts):
    def __init__(self, author,image):
        super().__init__(author)
        self.image = image
        self.username = self.author._userName


    def display(self):
        img = mpimg.imread(self.image)
        plt.imshow(img)
        plt.show()
        print("Shows picture")

    def __str__(self):
        return f"{self.username} posted a picture\n"



class SalePost(Posts):
    def __init__(self, author, name, price, location):
        super().__init__(author)
        self.username = author._userName
        self.name = name
        self.price = price
        self.location = location
        self.is_sold= False

    def discount(self, percentage, password):
        if password == self.author.get_password() and self.author.is_online():
            self.price =self.price*(1-percentage/100)
            print(f"Discount on {self.username} product! the new price is: {self.price}")
    def sold(self, password):
        if password == self.author.get_password() and self.is_sold==False and self.author.is_online():
            self.is_sold = True
            print(f"{self.username}'s product is sold")

    def __str__(self):
        if(self.is_sold):
            return f"{self.username} posted a product for sale:\nSold! {self.name}, price: {self.price}, pickup from: {self.location}\n"
        else:
            return f"{self.username} posted a product for sale:\nFor sale! {self.name}, price: {self.price}, pickup from: {self.location}\n"

