import re

imaliStaffs = "sean" "nelly" "scentry" "eunice"
checkingForStaffs = r"eunice"
# searchForTheName = re.search(checkingForStaffs, imaliStaffs)
if re.search(checkingForStaffs, imaliStaffs):
    print( re.search(checkingForStaffs, imaliStaffs).group(), "the person in particlar is part of the staff")
else:
    print("not a staff")