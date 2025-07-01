x = int(input("Enter the number X: "))
y = int(input("Enter the number Y: "))
z = int(input("Enter the number Z: "))

if x > y and x > z:
    print("X is largest")
elif y > x and y > z:
    print("Y is largest")
else:
    print("Z is largest")