list1 = [1,2,3,4,5]
print(list1)

list1.append(6)
print(list1)

list1.pop(1)
print(list1)

sum = 0
n = len(list1)  

for i in range(n):
    sum = sum + list1[i]
print(f"The sum of the list is {sum}")