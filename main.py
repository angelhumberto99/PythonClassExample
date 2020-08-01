#this is an example of packages and classes on python

#including the person class as a package
from include.Person import *

def main():
    p = Person()

    #setting an object
    p.SetName("Ángel")
    p.SetAge(20)
    p.SetHeight(1.70)
    p.SetWeight(72.1)
    
    #passing the object as a parameter
    ShowStatus(p)

    print("-.-.-.-.-.-.-.-.-.-.-.-.-")
    #using the Status method 
    p.Status()


def ShowStatus(obj):
    #printing the class members, using getters
    print("Name: ", obj.GetName(),
              "\nAge: ", obj.GetAge(),
              "\nWeight: ", obj.GetWeight(),
              "\nHeight: ", obj.GetHeight())

#this macro is used to start the program
#in the main function as default
if __name__ == "__main__":
    main()