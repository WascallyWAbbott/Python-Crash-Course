# Use f strings

first_name = "Wes"
last_name = "Abbott"
full_name = f"{first_name} {last_name}"
print(full_name)

# using variable with strings

print(f"Hello", full_name.title())

# f string to compose message, then assign entire message to a variable

message = f"Hello, {full_name.title()}"
print(message)
