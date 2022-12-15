print("Type NEW to create a new document.")
print("Type SAVECLOSE to save & close.")
print("Type OPEN to open.")
print("Type NAME to rename.")
print("Type EDIT to edit.")
DocNameList = []
Line = ""
LineCount = 1
CurrentDoc = ""
Writing = 0
DocName = ""
DocListContents = []

def ASK():
    global CurrentDoc
    global LineCount
    global Line
    global DocName
    global Writing
    StartOption = ""
    while StartOption != "SAVE" or StartOption != "NEW" or "EDIT" or StartOption != "OPEN" or StartOption != "NAME" or StartOption != "SAVECLOSE":
        StartOption = input("Enter:")
        if StartOption == "NEW":
            LineCount = 1
            DocName = input("Document Name:")
            Writing = 0
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
        if StartOption == "SAVECLOSE":
            SAVECLOSE()

def SAVECLOSE():
    global CurrentDoc
    global DocName
    global Writing
    DocListContents.append[CurrentDoc]
    CurrentDoc = []
    DocName = ""
    Writing = 0
    StartOption = ""
    ASK()


def NEW():
    global CurrentDoc
    global Writing
    global LineCount
    while Writing == 0:
        print(f"Line {LineCount}:")
        Line = input(f"\n")
        CurrentDoc.append(f"{Line}\n") 
        LineCount += 1
        if "HOME" in Line:
            ASK()

def EDIT():
    global CurrentDoc
    Editing = True
    while Editing == True:
        EditLine = int(input("Line (int) you want to replace:"))
        while EditLine <= len(CurrentDoc):
            ReplaceLine = input("Replace contents:")
            if "HOME" in ReplaceLine:
                ASK()
                Editing = False
            else:
                CurrentDoc[EditLine] = ReplaceLine
                print(f"Edited line {CurrentDoc[EditLine]}")
                print("Edit complete next line")


ASK()




























