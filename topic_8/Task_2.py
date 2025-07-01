x = float(input("Enter the CGPA of X: "))
y = float(input("Enter the CGPA of Y: "))
z = float(input("Enter the CGPA of Z: "))

if x < y and x < z:
    print("X has low CGPA")
elif y < x and y > z:
    print("Y has low CGPA")
else:
    print("Z has low CGPA")
    
avg = (x + y + z) / 3
print(f"The average CGPA is {avg:.2f}")