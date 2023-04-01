# Aleckxis Kate V. Bernabe
# BSCPE 1-4

# Problem 3

# Ask the plaintext message and keyword from the user.
plain_text = input("Enter the plaintext message:")
keyword = input("Enter the keyword:")

# Convert the keyword to corresponding letter values 0-25.
keyword_value = [ord(letter) - ord('A') for letter in keyword]

# Apply the Vigenère cipher to generate the ciphertext.
cipher_text = ''.join(chr((ord(letter) - ord('A') + keyword_value[index % len(keyword)]) % 26 + ord('A')) for index, letter in enumerate(plain_text))

# Print the resulting ciphertext.
print("Ciphertext:", cipher_text)