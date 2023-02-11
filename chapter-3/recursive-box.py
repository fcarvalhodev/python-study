#The code is a recursive function that searches for an object with the "is_a_key" method
#inside a box object. The box object must contain other objects that can either be boxes or keys.
#Time complexity is O(n) as the function needs to traverse all elements in the worst-case scenario.
#Space complexity is O(n) as well, as it needs to store the calls to the function in the call stack.

class Item:
    def is_a_key(self):
        return False

class Box(Item):
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return iter(self.items)

class Key(Item):
    def is_a_key(self):
        return True


def search_for_the_key(item):
    if isinstance(item, Key) and item.is_a_key():
        print("Found the key!")
        return
    elif isinstance(item, Box):
        for sub_item in item:
            search_for_the_key(sub_item)
    else:
        print("Item is not a key or a box.")

items = [1, 2, 3, Key(), 4, 5, 6, Box([7, 8, 9, Key(), 10])]
box = Box(items)
search_for_the_key(box)