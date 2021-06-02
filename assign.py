"""import camelcase

x = camelcase.CamelCase()

list = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    element = (input())
    list.append(element)

print(list)
print(x.hump(list))"""

import camelcase

x = camelcase.CamelCase()

a = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    element = (input("enter the names: "))
    a.append(element)

print(a)

print(x.hump(a))