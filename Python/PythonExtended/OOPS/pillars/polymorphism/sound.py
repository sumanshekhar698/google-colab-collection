class Dog:
    def speak(self):
        return "Woof Woof"


class Cat:
    def speak(self):
        return "Meow Meow"


class Robot:
    def speak(self):
        return "BEEP BEEP"


def make_it_talk(thing):
    print(f"  {type(thing).__name__:<8} says {thing.speak()}")



for obj in (Dog(), Cat(), Dog(), Robot()):
    print(id(obj))
    make_it_talk(obj)