number = int(input('Enter a number: '))
n1 = number % 10
n2 = number //10 % 10
n3 = number // 100 % 10
n4 = number  // 1000 % 10
n5 = number // 10000
print(n1, n2, n3, n4, n5, sep ="\n")