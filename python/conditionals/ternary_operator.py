# Conditional Expressions (Ternary Operator), python supports one line conditionals.

age = int(input("Enter you age: "))

status = "Adult" if age >= 18 else "Minor"
print(status)


nmb = int(input("Enter the number to know your grade: "))

result = "Grade A" if nmb >= 90 else "Grade B" 
print(result)