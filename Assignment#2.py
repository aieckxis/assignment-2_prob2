# Aleckxis Kate V. Bernabe
# BSCPE 1-4

# Problem 2

# Ask the user to input the encrypted text.
encrypted_text = input("Enter a string to descrypt: ")

# Set an empty string for the plain text.
plain_text = ""

# Replace each character in encrypted text with corresponding vowel character.
#   if *, change to a
#   if &, change to e
#   if #, change to i
#   if +, change to o
#   if !, change to u
for char in encrypted_text:
    if char == "*":
        plain_text += "a"
    elif char == "&":
        plain_text += "e"
    elif char == "#":
        plain_text += "i"
    elif char == "+":
        plain_text += "o"
    elif char == "!":
        plain_text += "u"
    else:
        plain_text += char

# Display the plain text
print("Plain text:", plain_text)
