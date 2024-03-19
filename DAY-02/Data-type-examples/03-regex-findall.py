import re

trainningDetails = "Python for DevOps Course"
lookForPattern = r"for"
searchForThePattern = re.search(lookForPattern, trainningDetails)
if searchForThePattern:
    print("Pattern found:", searchForThePattern.group())
else:
    print("Pattern not found")