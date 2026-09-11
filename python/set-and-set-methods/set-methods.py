# Set Methods

items = {"Apples", "Banana", "Orange"}   # Sets does not support indexing or slicing cause sets are unordered, To access elements you must create a loop through sets.
for item in items:
    print(item)


fruits = {"Apple", "Banana"}
fruits.add("Orange")   # .add, adds the element to the set.
fruits.update(["Strawberry", "Guava"])   # .update updates the elements, the set with the content of the lists.
print(fruits)

numbers = {98, 99, 101, 333, 404, 1, 23, 46}
numbers.remove(98)   # .remove, removes the element from the list.
numbers.discard(505)   # .discard,  removes the element if present otherwise if not it will not show an error.
nm = numbers.pop()   # .pop, pop removes a random element from the set.
print(nm)
print(numbers)

vegies = {"Brinjal", "Tomato", "Carrot"}
vegies.clear()   # .clear, clears the set by removing every single element in the set.
print(vegies)
