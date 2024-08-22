ARN = "                      123456798/EUNICE"
# Test = ARN.strip()
# print (Test)
print (ARN.lower().strip())
print (len(ARN.split("/")[1]))  ## string inbuilt functions using split and lower


FirstName = "eunice"
LastName = "Adebukola"

FullName = FirstName + " " + LastName

print(FullName)

## MATCH

import re

text = "today is sucessful"

pattern = r"today1"

search = re.match( pattern, text)

if search:
    print("that exist")
else:
    print("none")



## REPLACE

Caption = "No more procastination today"


replace = r"today"

ToThis = "this week"

Complet = re.sub(replace, ToThis, Caption)


if Complet:
    print(Complet)

else:
    print("none of it")


## SEARCH


Searching = "eunice" "bukky" "tope"

Check = r"tope"

replace = "john"

# if Check:
#     print( re.search(Check, Searching).group(), "is found and it is being replace with", 
#           re.sub(Check, replace, Searching).replace('"', '').split())
if re.search(Check, Searching):
    found = re.search(Check, Searching).group()
    replaced_string = re.sub(Check, replace, Searching)
    # Split the string into a list
    result_list = replaced_string.replace('"', '').split(" , ")
    
    print(f"{found} is found and it is being replaced with", result_list)
else:
    print("not found")


Current = "my current state is ilorin but i was at Ilorin before actually"

Change = r"ilorin"

ToThis = "lagos"

print("the full sentence is:", re.sub(Change, ToThis, Current).upper())


