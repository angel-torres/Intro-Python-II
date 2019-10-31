# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, *args):
        self.args = args

    def __str__(self):
        s = f"Room: Description: {self.args}"
        return s

