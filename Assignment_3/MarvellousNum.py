def ChkPrime(Value):
    if(Value <= 1):
        return False
    for i in range(2,Value):
        if(Value % i == 0):
            return False
    return True