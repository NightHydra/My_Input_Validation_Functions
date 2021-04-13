def get_yes_no(init_statement, not_valid_statement="You must either input \
either yes or no"):

    while True:
        choice = input(init_statement)
        if choice.lower() == "y" or choice.lower() == "yes":
            return ('yes')
        elif choice.lower() == "n" or choice.lower() == "no":
            return ('no')
        else:
            print (not_valid_statement.replace("\input", choice))



def get_valid_choice(init_statement, *args, case_sensitive = True, \
                     not_valid_statement = "Not Valid"):

    choice = input(init_statement)
    original = choice

    if case_sensitive == False:
        choice = choice.lower()
        args = tuple([i.lower() for i in args])

    while choice not in args:
        
            print (not_valid_statement.replace("\input", choice))

            choice = input(init_statement)
            original = choice
            if case_sensitive == False:
                choice = choice.lower()
    return original

def validation_with_function(init_statement, functions, *args,\
                             not_valid_statement = "Not Valid"  ):
    # To use methods that require perameters put function as
    #  'lambda var_name: var_name.method'
    choice = input(init_statement)
    mod_choice = choice
    for func in functions:
        mod_choice = func(mod_choice)

    while mod_choice not in args:
        
            print (not_valid_statement.replace("\input", str(choice)))

            choice = input(init_statement)
            mod_choice = choice
            for func in functions:
                mod_choice = func(mod_choice)
    return choice


def valid_num(x, is_int = False, is_pos = False, is_neg = False, domain = "(-inf, inf)"): 
    
    # Checks a variety of things about a string to see what type of number it is
    
    ret = False
            

    try: #Makes sure it can be a float
        x = float(x)
        ret = True
    except ValueError:
        
        return False

    if is_int == True:
        if float(x) != int(float(x)):
            ret = False
    
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

