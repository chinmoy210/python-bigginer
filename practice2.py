# Multiplication table of a given number input by the user of this python program

def Multitable(n):
    for i in range(1, 10+1):
        s = f"{n} * {i} = {n*i}"
        print(s)
        f = open('text1.txt', 'a')
        f.write(s)
        f.close

if __name__ == "__main__":
    n = int(input("Enter the number to show multiplication table "))
    Multitable(n)