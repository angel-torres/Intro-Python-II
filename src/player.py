# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.inventory = []

    def __str__(self):
        s = f"Player: {self.name}, location: {self.location}"
        return s

