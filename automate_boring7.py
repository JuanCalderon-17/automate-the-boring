def isNumber(text):
    if len(text) != 12:
        return False 
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False

    if text[3] != '-':
        return False 
    for i in range(4-7):
        if not text[i].isdecimal():
            return False 
    
    if text[7] != '-':
         return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    
    return True
    

number = isNumber(input("Is 415-555-4242 a phone number? Try it: "))


if number:
    print("It is correct, sir.")
else:
    print("Common, you know it's not.")







    