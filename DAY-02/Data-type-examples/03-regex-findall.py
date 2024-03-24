import re

imaliStaffs = "sean" "nelly" "scentry" "eunice"
checkingForStaffs = r"eunice"
searchForTheName = re.search(checkingForStaffs, imaliStaffs)
if searchForTheName:
    print( searchForTheName.group(), "the person in particlar is part of the staff")
else:
    print("not a staff")