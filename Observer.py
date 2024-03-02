class Observer:

    def __init__(self, name):
        self.notifications = []
        self.name = name

    def add_notification(self, notification):
        self.notifications.append(notification)

    def like_post(self, Observer):
        if self.name != Observer.name:
            Observer.add_notification(f"{self.name} liked your post")
            print(f"notification to {Observer.name}: {self.name} liked your post")

    def comment_post(self, Observer, comment):
        if self.name != Observer.name:
            Observer.add_notification(f"{self.name} commented on your post")
            print(f"notification to {Observer.name}: {self.name} commented on your post: {comment}")

    def __str__(self):
        ans = f"{self.name}'s notifications:"
        for notification in self.notifications:
            ans += "\n" + notification
        return ans


class Publisher:

    def __init__(self, name):
        self.observers = []
        self.name = name

    "Attach"

    def add_observer(self, Observer):
        if Observer not in self.observers:
            self.observers.append(Observer)
            print(f"{Observer.name} started following {self.name}")

    "Detach"

    def remove_observer(self, Observer):
        if Observer in self.observers:
            self.observers.remove(Observer)
            print(f"{Observer.name} unfollowed {self.name}")

    def update_new_post(self, new_post):
        for observer in self.observers:
            observer.add_notification(f"{self.name} has a new post")
        "Check"
        print(new_post)

    def num_followers(self):
        return len(self.observers)
