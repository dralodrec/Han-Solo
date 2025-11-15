def Freceipt(value1, value2="", value3=""):
    # get the initials from value1 (string)
    letters = []
    for words in value1.split():
        letters.append(words[0:1])
    
    # get the first 2 characters of value1 (string)
    if len(letters) >= 2:
        value1 = letters[0].upper() + letters[1].upper()
    else:
        value1 = letters[0].upper()

    # get the 3 middle characters of value2 (string)
    value2 = value2[2:5].upper()

    # get the last 4 characters of value3 (string)
    value3 = value3[-4:]

    if value2 == "" and value3 == "":
        newValue = value1
    else:
        newValue = value1 + "-" + value2 + "-" + value3
    print(newValue)

Freceipt("john smith")