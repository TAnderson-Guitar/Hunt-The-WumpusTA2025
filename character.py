"""Character class for Hunt the Wumpus"""
class Character:
    """Defines attributes and methods for Character objets"""
    def __init__(self, char_name, char_description):
        """Sets the class attributes"""
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        """Displays informaiton about the character"""
        print(self.name + " is here!")
        print(self.description)

    def set_conversation(self, conversation):
        """Method to set what the character can say"""
        self.conversation = conversation

    def talk(self):
        """Method to make the character talk"""
        if self.conversation is not None:
            print(self.name + " says: " + self.conversation)
        else:
            print(self.name + " does not want to talk to you.")

    def fight(self):
        """Method to make the character fight you"""
        print(self.name + " does not want to fight you.")
        return True
