# Checks if x is prime
def isPrime(x):
    if not type(x) == int:
        raise TypeError("isPrime only takes positive non-zero integers but a non-integer was provided")
    elif x < 0:
        raise TypeError("isPrime only takes positive non-zero integers but a negative integer was provided")
    elif x == 0:
        raise TypeError("isPrime only takes positive non-zero integers but zero was provided")
    if x == 1:
        return False
    elif x == 2:
        return True
    else:
        for n in range(2, x):
            if x % n == 0:
                return False
        return True

# Gets user's number
while True:
    while True:
        try:
            print(" \n Type 0 to quit \n ")
            N = int(input("Please input a positive non-zero non-prime number: "))
            if N == 0:
                break
            if not type(N) == int:
                print("Not an integer")
            elif N < 2:
                print("Not more than 1")
            elif isPrime(N):
                print("Not prime please")
            else:
                break
        except TypeError:
            print("Not a number")

    # Get all the prime factors
    if N == 0:
        break
    factors = []
    for n in range(2, N):
        if isPrime(n) and N % n == 0:
            factors.append(n)
        n += 1

    # Check how many times each prime factor divides into the user's number
    counts = []
    for x in factors:
        M = N
        counter = 0
        while M % x == 0:
            M /= x
            counter += 1
        counts.append(counter)

    # Print the result
    line = ""
    for i in range(0, len(factors)):
        if not i == len(factors) - 1:
            line += str(factors[i]) + "^" + str(counts[i]) + " * "
        else:
            line += str(factors[i]) + "^" + str(counts[i])
    print(line)

# Quit
quit()