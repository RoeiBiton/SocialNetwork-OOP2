class Observer:
    """
    Represents an observer who receives notifications about posts.

    This class implements the Observer design pattern.
    
    Attributes:
        notifications (list): A list to store notifications.
        name (str): The name of the observer.
    """

    def __init__(self, name):
        """
        Initializes an Observer object with the given name.

        Parameters:
            name (str): The name of the observer.
        """
        self.notifications = []
        self.name = name

    def add_notification(self, notification):
        """
        Add a notification to the observer's notifications list.

        Parameters:
            notification (str): The notification to be added.
        """
        self.notifications.append(notification)

    def like_post(self, Observer):
        """
        Like a post of another observer.

        Parameters:
            Observer (Observer): The observer whose post is being liked.
        """
        if self.name != Observer.name:
            Observer.add_notification(f"{self.name} liked your post")
            print(f"notification to {Observer.name}: {self.name} liked your post")

    def comment_post(self, Observer, comment):
        """
        Comment on a post of another observer.

        Parameters:
            Observer (Observer): The observer whose post is being commented on.
            comment (str): The comment to be added to the post.
        """
        if self.name != Observer.name:
            Observer.add_notification(f"{self.name} commented on your post")
            print(f"notification to {Observer.name}: {self.name} commented on your post: {comment}")

    def __str__(self):
        """
        Return a string representation of the observer's notifications.

        Returns:
            str: A string representation of the observer's notifications.
        """
        ans = f"{self.name}'s notifications:"
        for notification in self.notifications:
            ans += "\n" + notification
        return ans


class Publisher:
    """
    Represents a publisher who shares posts and notifies observers about them.

    This class implements the Observer design pattern.

    Attributes:
        observers (list): A list to store observers following the publisher.
        name (str): The name of the publisher.
    """

    def __init__(self, name):
        """
        Initializes a Publisher object with the given name.

        Parameters:
            name (str): The name of the publisher.
        """
        self.observers = []
        self.name = name

    def add_observer(self, Observer):
        """
        Add an observer to the list of followers.

        Parameters:
            Observer (Observer): The observer to be added.
        """
        if Observer not in self.observers:
            self.observers.append(Observer)
            print(f"{Observer.name} started following {self.name}")

    def remove_observer(self, Observer):
        """
        Remove an observer from the list of followers.

        Parameters:
            Observer (Observer): The observer to be removed.
        """
        if Observer in self.observers:
            self.observers.remove(Observer)
            print(f"{Observer.name} unfollowed {self.name}")

    def update_new_post(self, new_post):
        """
        Notify all followers about a new post.

        Parameters:
            new_post : The new post to be shared.
        """
        for observer in self.observers:
            observer.add_notification(f"{self.name} has a new post")
        print(new_post)

    def num_followers(self):
        """
        Get the number of followers.

        Returns:
            int: The number of followers.
        """
        return len(self.observers)
