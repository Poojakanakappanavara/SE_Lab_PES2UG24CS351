with open("PES2UG24CS351.txt", "r") as file:
    text = file.read().lower()

with open("key.txt", "r") as file:
    key = file.read()

alphabet = "abcdefghijklmnopqrstuvwxyz"

ciphertext = ""

for ch in text:
    if ch in alphabet:
        ciphertext += key[alphabet.index(ch)]
    else:
        ciphertext += ch

print("Ciphertext:")
print(ciphertext)

with open("ciphertext.txt", "w") as file:
    file.write(ciphertext)