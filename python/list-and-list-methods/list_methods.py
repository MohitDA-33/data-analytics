# List Methods, by using methods you can add, remove or change an existing element, and remember any method we use or run changes the actual/original list.



fruits = ["Apple", "Banana", "Guava"]
more_fruits=["Peaches", "Oranges"]

print(len(fruits))   # Len function tell you about the number of elements in a list, by counting the elements.

fruits.append("Grapes")   # .append, adds an element to the end of the list.
print(fruits)

fruits.insert(1, "Strawberry")   # .insert adds an element at the given index, here its index no 1.
print(fruits)

fruits.extend(more_fruits)   # .extend adds elements from the other given list, and gives you a final list.
print(fruits)

fruits.remove("Guava")   # .remove, removes the element from the list.
print(fruits)

fruits.pop()   # .pop removes the last element from the list.
print(fruits)
fruits.pop(2)   # In .pop by telling the index number you can remove a specific element.
print(fruits)

print("Strawberry" in fruits)
print("Strawberry" not in more_fruits)

fruits.clear()   # .clear, clears/empties the list.
more_fruits.clear()
print(fruits)
print(more_fruits)



names = ["Mohit", "Rohit", "Nohit", "ohit", "Rohit"]
more_names = ["Aditi", "Sakshi"]

print(names.index("Rohit"))   # .index, tells you about the index number of an element, but only the first occurance if there are two rohit it will only return the first occurance and not the other one.

print(names.count("Rohit"))   # .count, counts the number of time a value appears.

new_names = more_names.copy()   # .copy returns a copy of the list.
print(new_names)

names.reverse()   # .reverse, reverses the order of the list.
print(names)

print("Akansha" in names)
print("Aditi" in more_names)



numbers = [59, 66, 79, 91, 1, 0, 3, 9, 39, 27]
numbers.sort()   # .sort, sorts the values in ascending order.
print(numbers)

numbers.sort(reverse = True)   # This will sort the values in descending order.
print(numbers)

print(91 in numbers)   # Use of membership operator.
