print("Type NEW to create a new document.")
print("Type CLOSE to close the document.")
print("Type SAVE to save.")
print("Type OPEN to open.")
print("Type NAME to rename.")
print("Type EDIT to edit.")
DocNameList = []
Line = ""
LineCount = 0
CurrentDoc = []
DocListAndContents = {}
Writing = 0
DocName = ""

def ASK():
    global LineCount
    global Line
    global DocName
    global Writing
    StartOption = ""
    while StartOption != "SAVE" or StartOption != "NEW" or "EDIT" or StartOption != "OPEN" or StartOption != "NAME":
        StartOption = input("Enter:")
        if StartOption == "NEW":
            LineCount = 0
            Line = ""
            DocName = input("Document Name:")
            Writing = 1
            DocNameList.append(DocName)
            NEW()
        if StartOption == "CLOSE":
            pass
        if StartOption == "NAME":
            pass
        if StartOption == "OPEN":
            pass
        if StartOption == "EDIT":
            EDIT()
def CLOSE():
    global CurrentDoc
    global DocName
    global Writing
    CurrentDoc = []
    DocName = ""
    Writing = 0
    StartOption = ""


def NEW():
    global Writing
    global LineCount
    while Writing == 1:
        Line = input()
        CurrentDoc.append(Line)
        LineCount += 1
        if "CLOSE" in Line:
            CLOSE()

def EDIT():
    CurrentDoc[2] = input("Enter:")

ASK()





















