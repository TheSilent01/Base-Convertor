# Welcome message
print("Welcome to The Base Converter")

# Input: Get the number from the user
number = int(input("Please input your chosen number: "))

# Convert the number to binary, hexadecimal, and octal
binary = bin(number)[2:]  # Remove the '0b' prefix
hexadecimal = hex(number)[2:]  # Remove the '0x' prefix
octal = oct(number)[2:]  # Remove the '0o' prefix

# Output the results
print(f"The number in binary is {binary}")
print(f"The number in hexadecimal is {hexadecimal}")
print(f"The number in octal is {octal}")
