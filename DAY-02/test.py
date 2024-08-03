
import re

FamilyName = "abiodun/adelola-bayo"

print(FamilyName.split("/") [0].upper())

Family = "abiodun"

FirstDaugther = "adelola"
Firstson = "adebayo"

fullDaughterName = Family + " " + FirstDaugther 
fullSonName = Family + " " + Firstson

surname = r'abiodun'

checking = re.match(surname, fullDaughterName)
checking = re.search(surname, fullDaughterName)

if checking:
    print(checking.group(), "surname is present in:", fullDaughterName)
else:
    print(checking.group(), "is not present here in the:", fullDaughterName)
print("               the name of the first daughter and the son are".strip(), 
      fullDaughterName.upper(), "and ",
      fullSonName.upper(), 
      "also the length of their names all together is", len(FirstDaugther), "for the daughter, and", len(Firstson), "for the son")

# // strp is to remove space 

AdeAge = 4.5
BayoAge = abs(-2.55)

Addition = AdeAge + BayoAge
Subtraction = AdeAge - BayoAge
Multiplication = AdeAge * BayoAge
Roundup = round(Addition, 1)


print ( "Addition is:", Addition)

print ("Subtration is :", Subtraction)
print("Multiplication is:", Multiplication)
print("roundfigure is:", Roundup)


Lagos = "i came to lagos last year july and resume to imalipay august"

pattern = r'imalipay'

PartOf = re.search ( pattern, Lagos)

replacement = "yolat"
slipting = ','

Nowchange = re.sub(pattern, replacement, Lagos)
Tosplit = re.split(slipting, Lagos)
print(Tosplit)
if Nowchange:
    print(Nowchange)
else:
    print("none")
if PartOf:
    print (PartOf.group(), "is part of the story")
else:
    print(PartOf.group(), "is not part of it")