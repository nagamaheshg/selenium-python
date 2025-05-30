fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed_list = ["John", 25, True, 5.9]

name = mixed_list[0]

print(fruits[0])
print(fruits[-1])

fruits.append("grapes")
fruits.insert(1, 'mango')
fruits.remove('banana')
popped_item = fruits.pop()
print(f'deleted item is {popped_item}')

fruits.append('cherry')
fruits.append("watermelon")
print(fruits)

print(fruits[1:])
print(fruits[::-1])

print(fruits[fruits.index('orange'):])

