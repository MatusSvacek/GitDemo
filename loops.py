greeting = "Good morning"

if greeting == "Good morning":
    print("condition matches")
else:
    print("condition does not match")

print("if else condition is complete")

#for loop

obj = [1, 2, 3, 4, 5, 6]

for i in obj:
    print(i)

# sum of first natural numbers 1+2+3+4+5 = 15

summation = 0
for j in range(1,6): #range (i,j) - iterate i to j-1
    summation = summation + j
print(summation)

print("************************")
for k in range(1, 10, 2):
    print(k)

print("************************") #skipping initial index
for g in range(10):
        print(g)