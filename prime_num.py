def prime_num(x):
    
    if not  isinstance(x, list):
        return "Only Integers allowed"
    
    elif x <= 0:
        return False
    else:
        for n in x:
            b = [2, 3]
            if n % 2 == 0 and n % 3 == 0:
                return False
            else:
                return b.append(n)
        
print prime_num([3, 5])



