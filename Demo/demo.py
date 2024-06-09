details = " adediran eunice"
firstName = "adediran"
middleName = "eunice"
fullName = firstName + " " + middleName
print (" my fullname is:",  fullName)

course = "            COMPUTER SCIENCE"
print (course.strip())
theLength = len(course)

print ( theLength)

print( " the student fullname is:".upper(), fullName, "and the length of the course she offers is:" , course.replace( "COMPUTER", "BIOLOGY").split())

substring = "eunice"

if substring in fullName:
    print ("the name:", substring, "is part of the student name")
else:
    print( "the name:", substring, "is not part of the student name")

balance = 24000
expenses = 12000

accountStatement = balance - expenses

print (accountStatement)

import sys
import re

def account( balance, expenses):
    return balance - expenses

print (account(50000, 25000))


coderDen = "ebuka" "tosin" "pauline" "rajah"

checkForstaff = r'tosin'

if re.search(checkForstaff, coderDen):
    print( "she is part of the den")
else:
    print("shes is not")