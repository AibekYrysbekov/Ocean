class student_room:
    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    def __str__(self):
        return f'<name:{self.name}, age:{self.age}, major:{self.major}>'
Steve = student_room("Steven Schultz", 23, "English")
Johnny = student_room("Jonathan Rosenberg", 24, "Biology")
Penny = student_room("Penelope Meramveliotakis", 21, "Physics")
print(Steve)
print(Johnny)
print(Penny)