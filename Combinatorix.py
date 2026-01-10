print("Let's solve some Combinatorics!!")

# ---------- basic functions ----------

def f(x):
    """factorial of x (x!)"""
    if x < 0:
        print("Factorial of", x, "is not defined.")
        return None
    k = 1
    for i in range(1, x + 1):
        k *= i
    return k

def c(n, r):
    """nCr = n! / (r!(n-r)!)"""
    if r < 0 or n < 0 or r > n:
        print("Invalid: n and r must satisfy 0 <= r <= n.")
        return None
    return f(n) // (f(r) * f(n - r))

def p(n, r):
    """nPr = n! / (n-r)!"""
    if r < 0 or n < 0 or r > n:
        print("Invalid: n and r must satisfy 0 <= r <= n.")
        return None
    return f(n) // f(n - r)

# ---------- arranging (permutations) ----------

def arrange():
    a = input("What are the items you want to arrange? ")
    b = int(input(f"How many {a} are there in total (n)? "))
    r = int(input(f"How many out of these {b} {a} do you want to arrange (r)? "))

    if r > b or r < 0:
        print("r must satisfy 0 <= r <= n.")
        return

    rep = input("Are repetitions allowed? (yes/no) ")

    if rep.lower() == "yes":
        # arrangements with repetition: n^r
        ways = b ** r
        print(f"The number of ways of arranging {r} {a} from {b} {a} with repetition is {ways}.")
        return

    # no repetition
    circ = input("Is the arrangement in a circle? (yes/no) ")
    if circ.lower() == "yes":
        if r == 0 or r == 1:
            ways = 1
        else:
            # circular permutations of r distinct objects = (r-1)!
            ways = f(r-1)
        print(f"The number of circular arrangements of {r} distinct {a} is {ways}.")
    elif rep.lower()==no or circ.lower()==no:
        ways = p(b, r)
        print(f"The number of ways of arranging {r} distinct {a} out of {b} {a} in a line is {ways}.")

# ---------- selecting (combinations) ----------

def select():
    d = input("What are the items you want to select? ")
    n = int(input(f"How many {d} are there in total (n)? "))
    r = int(input(f"How many out of these {n} {d} do you want to select (r)? "))

    if r > n or r < 0:
        print("r must satisfy 0 <= r <= n.")
        return

    rep = input("Are repetitions allowed in selection? (yes/no) ")

    if rep.lower() == "no":
        # simple nCr
        g = c(n, r)
        print(f"The number of ways of selecting {r} {d} out of {n} {d} is {g}.")
    elif rep.lower()=="yes":
        # combinations with repetition: C(n+r-1, r)
        g = c(n + r - 1, r)
        print(f"The number of ways of selecting {r} {d} from {n} {d} with repetition is {g}.")

# ---------- grouping (unordered groups) ----------

def groupf():
    sizes = []
    I = input("What are the items you want to group? (all items are considered distinct) ")
    h = int(input(f"Enter the number of {I} available: "))
    g = int(input("Enter how many groups you want to form: "))

    total = 0
    print("Enter sizes of each group (sum must be equal to total items):")
    for i in range(g):
        s = int(input(f"  Size of group {i + 1}: "))
        sizes.append(s)
        total += s

    if total != h:
        print(f"The sizes you entered sum to {total}, but there are {h} {I}. Please try again.")
        return

    # formula: h! / Π ( (size_i!) * (count_of_groups_with_this_size)! )
    denom = 1
    for s in set(sizes):
        m = sizes.count(s)
        denom *= (f(s) ** m) * f(m)

    W = f(h) // denom
    print(f"You can split {h} distinct {I} into the specified groups in {W} different ways.")

# ---------- distributing into labelled groups ----------

def groupd():
    sizes = []
    I = input("What are the items you want to distribute? (all items are considered distinct) ")
    h = int(input(f"Enter the number of {I} available: "))
    g = int(input("Enter how many groups you want to form: "))

    total = 0
    print("Enter sizes of each group (sum must be equal to total items):")
    for i in range(g):
        s = int(input(f"  Size of group {i + 1}: "))
        sizes.append(s)
        total += s

    if total != h:
        print(f"The sizes you entered sum to {total}, but there are {h} {I}. Please try again.")
        return

    denom = 1
    for s in set(sizes):
        m = sizes.count(s)
        denom *= (f(s) ** m) * f(m)

    # first count ways to form unlabelled groups
    W = f(h) // denom
    # labels for g groups: multiply by g!
    DW = W * f(g)

    print(f"You can distribute {h} distinct {I} into the specified labelled groups in {DW} different ways.")

# ---------- menu ----------

def main():
    while True:
        print("\n----- Combinatorics Menu -----")
        print("1. Factorial")
        print("2. nCr (Combination)")
        print("3. nPr (Permutation)")
        print("4. Arrange objects")
        print("5. Select objects")
        print("6. Group objects (unlabelled groups)")
        print("7. Distribute objects (labelled groups)")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            n = int(input("Enter n: "))
            print("Factorial =", f(n))

        elif choice == "2":
            n = int(input("Enter n: "))
            r = int(input("Enter r: "))
            print("nCr =", c(n, r))

        elif choice == "3":
            n = int(input("Enter n: "))
            r = int(input("Enter r: "))
            print("nPr =", p(n, r))

        elif choice == "4":
            arrange()

        elif choice == "5":
            select()

        elif choice == "6":
            groupf()

        elif choice == "7":
            groupd()

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

# run the menu
if __name__ == "__main__":
    main()
