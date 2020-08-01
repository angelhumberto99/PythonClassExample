class Person:
    def __init__(self):
        #if we use double underscore before the name of the class members
        #they will be private for the class 
        self.__name = ""
        self.__age = 0
        self.__weight = 0.0
        self.__height = 0.0

    def Status (self):
        print("Name: ", self.__name,
              "\nAge: ", self.__age,
              "\nWeight: ", self.__weight,
              "\nHeight: ", self.__height)

    #setters
    def SetName(self, value):
        self.__name = value

    def SetAge(self, value):
        self.__age = value

    def SetWeight(self, value):
        self.__weight = value

    def SetHeight(self, value):
        self.__height = value

    #getters
    def GetName(self):
        return self.__name

    def GetAge(self):
        return self.__age

    def GetWeight(self):
        return self.__weight

    def GetHeight(self):
        return self.__height

