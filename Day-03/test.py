# global and local variable

## global

FirstName = "Eunice"
MiddleName = "adebukola"


def concantination():
    print(FirstName + " " + MiddleName.upper())

concantination()


surname = "Adediran" #global variable

def firstBorn():
    firstBorn = "tunde" #local variable
    SecondBorn = "tayo"
    fullName = surname + " " + firstBorn

    print ("the full name of the first born is", fullName)

def secondBorn():
    SecondBorn = "tit"
    print( surname + " " + SecondBorn )

firstBorn()
secondBorn()