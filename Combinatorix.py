print("Let's solve some Combinatorics!!")

def f(x):
    if x>0:
        i=1
        k=1
        for j in range(x):
            k=i*k
            i=i+1
        return k
    elif x==0:
        return 1
            
    else:
        print("factorial of ", x, " is not defined", sep="")
    

def c(x,y):
    return int(f(x)/(f(y)*f(x-y)))

def p(x,y):
    return int(f(x)/f(x-y))

def arrange():
    arr=[]
    ts=0
    a=input("what are the items, you want to arrange? ")
    b=int(input(f"how many {a} are there? "))
    C=int(input(f"how many out of {b} {a} you want to arrange? "))
    D=input(f"are all the {C} {a} distinct? ")    
    if D.lower=="yes":
        return f"the number of ways of arranging {C} distinct {a} out of {b} {a} is {p(b, C)}"
    elif D.lower=="no":
        E=int(input("enter number of distinct objects"))
        if E==C:
            return f"the number of ways of arranging {C} distinct {a} out of {b} {a} is {p(b, C)}"
        elif E>C:
            return "try again"
        elif E<C:
            F=int(input(f"how many different groups of {a} are present? "))
            for items in range(F):
                item=int(input(f"{items+1}: enter the number of {a} present: "))
                arr.append(item)
                ts+=item
            if ts!=C:
                print(f"total can't be more than {C}. Aborting!!!")
            elif ts==C:
            
                    
        
def select():
    d=input("what are the items, you want to select? ")
    e=int(input(f"how many {d} are there? "))
    f=int(input(f"how many out of {e} {d} you want to select? "))

    g=c(e, f)

    return(f"the number of ways of selecting {f} {d} out of {e} {d} is {g}. ")

def groupf():
    sizes = []
    I = input("What are the items you want to group?")
    h = int(input(f"Enter the number of {I} available: "))
    g = int(input("Enter how many groups you want to form: "))

    total = 0
    for i in range(g):
        s = int(input(f"  size of group {i + 1}: "))
        sizes.append(s)
        total += s

    if total != h:
        print(f"The sizes you entered sum to {total}, "
              f"but there are {h} {I}.  Please try again.")
        return None
    denom = 1
    for s in set(sizes):
        m = sizes.count(s)
        denom *= (f(s) ** m) * f(m)

    W = f(h) // denom

    return(f"You can split {h} distinct {I} into the specified "
          f"groups in {W} different ways.")
            
        
        
    



            