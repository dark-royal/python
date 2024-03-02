class Human:
    number_of_eyes = 2

    def __init__(self, height: float, gender: str, name: str):
        self.height = height
        self.gender = gender
        self.name = name

    def __str__(self):
        return f"{self.name} {self.gender}"
    def sleep(self):
        print(f"{self.name} sleeping........")

    def eat(self):
        print("eating.....")


bolaji = Human(4.5, "male","praise")
hannah = Human(3.5, "female", "israel")
print(hannah.number_of_eyes)
print(bolaji.number_of_eyes)
print(hannah.sleep())
print(bolaji.sleep())
print(hannah)

name = "dayo"

print(type(name))
print(type(bolaji))
