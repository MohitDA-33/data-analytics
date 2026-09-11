a = {99, 303, 505, 1001, 1, 5}
b = {1, 5, 707, 900, 2002}

print(a)
print(b)

un = a.union(b)   # .union, union combines the elements of the both the set and removes the duplicates.
print(un)

inter = a.intersection(b)   # .intersection, intersection prints the common elements.
print(inter)

diff = a.difference(b)   # .difference, prints the elements that are in set and not in b.
print(diff)

sys = a.symmetric_difference(b)   # .symmetric_difference, prints the elements that are in either set but not in both.
print(sys)

names = {"Mohit", "Rohit", "Nohit"}
print("Mohit" in names)   # Using membership operator to check if the element is present in the set or not.
print("Harry" in names)