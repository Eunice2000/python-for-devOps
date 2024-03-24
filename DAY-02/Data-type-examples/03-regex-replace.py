import re
theCompleteWord = "python is a programming culture"
thePattern = r"culture"
theWordToReplacwWith = "language"
replacingTheWord = re.sub(thePattern, theWordToReplacwWith, theCompleteWord) 
print("modified text:", replacingTheWord)