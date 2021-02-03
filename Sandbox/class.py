class Person:
    """ A basic class that stores names and birthday. 
    Class can retrieve a person's name piecewise and get their age."""

    def __init__(self, full_name, birthday):
        # extracts first and last names
        name_pieces = full_name.split(" ")
        self.firstName = name_pieces[0]
        self.lastName = name_pieces[-1]
        self.birthday = birthday   # yyyymmdd
    

    def birthday(self):
        components = str(self.birthday[1:4], )
        components[0] = self.birthday[1:4]
        components[1] = self.birthday[5:6]
        components[2] = self.birthday[7:8]
        return str(components[1] + "/" + components[2] + "/" + components[0])



fullName = input("Enter this person's full name: ")
birthday = input("Enter this person's birthday yyyymmdd: ")

person1 = Person(fullName, birthday)

print(person1.firstName)
print(person1.lastName)
print(person1.birthday())

help(Person)