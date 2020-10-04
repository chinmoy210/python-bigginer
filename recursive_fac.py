def fac1(n):
    if n == 1 or n == 0:
        return 1
    return n * fac1(n-1)

if __name__ == "__main__":
    n = int(input("Enter the number\n"))
    result = fac1(n)
    print(f"The factorial of {n} is {result}")