# :::ENUMERATE method:::
# Enumerate() method can create a list of the elements with its index numbers
fruit_list = ['Apple', 'Berry', 'pear', 'orange', 'tangerine']
for i, elements in enumerate(fruit_list):
    print(i, elements)

# you can change the index numbers of the list
for j, elements in enumerate(fruit_list, 100):
    print(j, elements)

# breaking a word by its letters
# you have to add 'list' before the enumerate keyword
fruitName= 'Jackfruit'
print(list(enumerate(fruitName)))