print('lists can be indexed and sliced')
squares = [1,4,9,16,25]
print(squares)

print('lists also support concatenation')
newSquares = squares + [36,49,64,81]
print(newSquares)

print('Unlike Strings lists are mutable ie it is possible to change their content')
cubes = [1,8,27,65,125]
print('Before Change')
print(cubes)
cubes[3] = 64
print('After Change')
print(cubes)
print('Using append to add new items to the end of list')
new_value = 216
cubes.append(new_value)
print(cubes)
cubes.append(7 **3)
print(cubes)

