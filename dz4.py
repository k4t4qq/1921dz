class Mother:
    name = "Sonya"
    age = "40"
class Father:
    familiya = "Kulik"
    age = "41"
class Brother(Father, Mother):
    eye_color = "Blue"
    name = "Tolik"
    def __init__(self):
        print(self.name)
        print(self.familiya)
        print(self.eye_color)
class Sister(Father, Mother):
    age = 12
    def __init__(self):
        print(self.name)
        print(self.familiya)
        print(self.age)
bro = Brother()
sis = Sister()
