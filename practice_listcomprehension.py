# Program for print a list of multiplication table of user entered number
n = int(input("Enter a number\n"))

list1 = [n*num for num in range(1, 11)]
print(list1)

f = open('Tables.txt', 'a')
f.write(str(list1)+"\n")
f.close()