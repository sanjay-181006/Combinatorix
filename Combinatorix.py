print("Let's solve some Combinatorics!!")

# ---------- basic math ----------

def factorial(n):
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def nCr(n, r):
    if r < 0 or r > n:
        raise ValueError("Require 0 ≤ r ≤ n")
    r = min(r, n - r)  # optimization
    num = 1
    den = 1
    for i in range(1, r + 1):
        num *= n - r + i
        den *= i
    return num // den


def nPr(n, r):
    if r < 0 or r > n:
        raise ValueError("Require 0 ≤ r ≤ n")
    result = 1
    for i in range(n, n - r, -1):
        result *= i
    return result


# ---------- helpers ----------

def get_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Please enter an integer.")
        return None


# ---------- arranging ----------

def arrange():
    item = input("What are the items you want to arrange? ")
    n = get_int(f"How many {item} are there in total (n)? ")
    r = get_int(f"How many out of these {n} {item} do you want to arrange (r)? ")

    if n is None or r is None or r < 0 or r > n:
        print("Invalid values.")
        return

    rep = input("Are repetitions allowed? (yes/no): ").lower()

    if rep == "yes":
        print(f"Ways = {n ** r}")
        return

    circ = input("Is the arrangement circular? (yes/no): ").lower()

    if circ == "yes":
        if r != n:
            print("Circular permutations require arranging all objects.")
            return
        print(f"Ways = {factorial(n - 1)}")
    else:
        print(f"Ways = {nPr(n, r)}")


# ---------- selecting ----------

def select():
    item = input("What are the items you want to select? ")
    n = get_int(f"How many {item} are there in total (n)? ")
    r = get_int(f"How many out of these {n} {item} do you want to select (r)? ")

    if n is None or r is None or r < 0 or r > n:
        print("Invalid values.")
        return

    rep = input("Are repetitions allowed? (yes/no): ").lower()

    if rep == "yes":
        print(f"Ways = {nCr(n + r - 1, r)}")
    else:
        print(f"Ways = {nCr(n, r)}")


# ---------- grouping ----------

def grouping(labelled=False):
    item = input("What are the items? (all distinct): ")
    n = get_int(f"Enter number of {item}: ")
    g = get_int("Enter number of groups: ")

    if n is None or g is None:
        return

    sizes = []
    print("Enter sizes of each group:")
    for i in range(g):
        s = get_int(f"  Size of group {i + 1}: ")
        if s is None:
            return
        sizes.append(s)

    if sum(sizes) != n:
        print("Group sizes must sum to total items.")
        return

    denom = 1
    for s in set(sizes):
        m = sizes.count(s)
        denom *= (factorial(s) ** m) * factorial(m)

    ways = factorial(n) // denom

    if labelled:
        ways *= factorial(g)

    print(f"Ways = {ways}")


# ---------- menu ----------

def main():
    while True:
        print("\n----- Combinatorics Menu -----")
        print("1. Factorial")
        print("2. nCr")
        print("3. nPr")
        print("4. Arrange objects")
        print("5. Select objects")
        print("6. Group objects (unlabelled)")
        print("7. Distribute objects (labelled)")
        print("0. Exit")

        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                n = get_int("Enter n: ")
                if n is not None:
                    print("Factorial =", factorial(n))

            elif choice == "2":
                n = get_int("Enter n: ")
                r = get_int("Enter r: ")
                print("nCr =", nCr(n, r))

            elif choice == "3":
                n = get_int("Enter n: ")
                r = get_int("Enter r: ")
                print("nPr =", nPr(n, r))

            elif choice == "4":
                arrange()

            elif choice == "5":
                select()

            elif choice == "6":
                grouping(labelled=False)

            elif choice == "7":
                grouping(labelled=True)

            elif choice == "0":
                print("Goodbye!")
                break

            else:
                print("Invalid choice.")

        except ValueError as e:
            print("Error:", e)


# ---------- run ----------

if __name__ == "__main__":
    main()
