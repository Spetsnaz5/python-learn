
# formatted-string-literals
user = "Bob"

print(f"Hello, {user}!")

# the-string-format-method
name = "Alice"
age = 30

print("My name is {} and I am {} years old.".format(name, age))

print("My name is {1} and I am {0} years old.".format(age, name))

print("My name is {name} and I am {age} years old.".format(name = "Alice", age = 30))