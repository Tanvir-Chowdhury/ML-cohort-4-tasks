dict1 = {
    "math": 90,
    "science": 85,
    "english": 92,
    "history": 88,
    "art": 95
}

print(dict1)

dict1["Bangla"] = 89

print(dict1)

dict1["english"] = 95

print(dict1)


sum = 0
for i,j in dict1.items():
    sum = sum + j
    
avg = sum / len(dict1)
print(f"The average marks is {avg:.2f}")