import random
import string

alphabet = list(string.ascii_lowercase)

key = alphabet.copy()
random.shuffle(key)

print("Substitution Cipher Key:")

for i in range(26):
    print(alphabet[i], "->", key[i])

with open("key.txt", "w") as file:
    file.write("".join(key))