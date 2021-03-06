class Dog:
    def __init__(self, name : str, month : int, day : int, year : int, speakText : str):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speakText = speakText

    def __add__(self, other):
        if type(other) == Dog:
            return Dogs(2, [self.name, other.name])
        if type(other) == Dogs:
            return Dogs(other.numDogs + 1, other.names.append(self.name))

class Dogs:
    def __init__(self, numDogs, names):
        self.numDogs = numDogs
        self.names = names

    def __str__(self):
        strinfo = "Number of dogs : " + str(self.numDogs) + "\n"
        strinfo = strinfo + "Names : " + str(self.names)
        return strinfo

    def __add__(self, other):
        if type(other) == Dog:
            return Dogs(self.numDogs + 1, self.names.append(other.name))
        if type(other) == Dogs:
            return Dogs(self.numDogs + other.numDogs, self.names.append(other.names))
