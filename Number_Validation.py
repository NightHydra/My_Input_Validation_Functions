def valid_num(x, is_int = False, is_pos = False, is_neg = False, domain = "(-inf, inf)"): 
    
    # Checks a variety of things about a string to see what type of number it is
    
    ret = False
            

    try: #Makes sure it can be a float
        x = float(x)
        ret = True
    except ValueError:
        
        return False
    
    
    if is_pos == True: # Checks to see if input is positive
        if float(x) <= 0:
            ret = False

    elif is_neg == True:
        if float(x) >= 0: #Checks to see if input is negative
            ret = False



    if not in_domain(float(x), domain): # Domain part
        ret = False

    return ret


def in_domain(x, domain): # Takes a domain and checks if x is in the domain
    # Uses interval notation (example - [0 - inf) is the domain of f(x) = sqrt(x) )
    dom = domain.replace(" ", "").split("U")
    ret = False
    for set_ in dom:
        
        l, r = set_.split(",")

        greater = False
        less = False
        
        if l[1::] == "-inf":
            greater = True

        else:
            if l[0] == "(":
                if x > float(l[1::]):
                    greater = True
            if l[0] == "[":
                if x >= float(l[1::]):
                    greater = True

        if r[:-1] == "inf":
            less = True

        else:
            if r[-1] == ")":
                if x < float(r[:-1]):
                    less = True
            if r[-1] == "]":
                if x <= float(r[:-1]):
                    less = True
        
        ret = ret or (greater and less)
        
    return ret
