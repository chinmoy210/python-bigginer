# a = int(input("Enter a "))
# b = int(input("Enter b "))

# try:
#     print(a/b)
# except ZeroDivisionError as e:
#     print("Infinite")   

# Enter your code here. Read input from STDIN. Print output to STDOUT
a = list(map(int, input("enter a nnumber \n").split()))
b = list(map(int, input("enter\n").split()))

a = set(a)
b = set(b)
print(a)
print(len(a.union(b)))









