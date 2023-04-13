number = list(range(20))
numbercopy = number
number1 = number[:]
print(id(number))
number.append(7)
print("number's id: " + str(id(number)))
print("numbercopy's id: " + str(id(numbercopy)))
print("number1's id: " + str(id(number1)))

i = 7
j = i 
print(str(id(i))+"\n"+str(id(j)))
i= i+1
print(j)
j = j-1
print(str(id(i))+"\n"+str(id(j)))
