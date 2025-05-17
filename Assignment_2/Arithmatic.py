def Add(No1 , No2):
    result = No1 + No2
    return result

def Sub(No1 , No2):
    result = No1 - No2
    return result

    # we can use logic written below if user wants only positive numbers
    #if (No1 < No2):
        #result = No2 - No1
    #else:
        #result = No1 - No2
    #return result

def Mult(No1 , No2):
    if((No1 == 0) | (No2 == 0)):
        print("Multiplication can not be done with zero, Enter valid numbers.")
        return
    else:
        result = No1 * No2
    return result

def Divide(No1 , No2):
    if(No2 == 0):
        print("Division is not possible with 0")
        return
    else:
        result = No1 / No2
    return result

