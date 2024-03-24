
# the above regression search for the word from the beginning and if not found it return the else  using the "match"
    # to be able to search for the word everywhere to match add "."

import re

handsOnLabOnMatch = "learning how the regression match works"
CheckingForThePattern = r".*works*"
usingTheMatchWord = re.match(CheckingForThePattern, handsOnLabOnMatch)
if usingTheMatchWord:
    print("match found:", usingTheMatchWord.group())
else:
    print("match not found")