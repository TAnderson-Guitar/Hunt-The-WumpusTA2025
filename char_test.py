"""character test space"""
from character import Enemy

harry = Enemy("Harry", "A dirty smelly Wumpus")
harry.describe()
harry.set_conversation("Come closer. I cannot see you.")
harry.talk()
print(harry)