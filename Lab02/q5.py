with open("ciphertext.txt", "r") as file:
    ciphertext = file.read()

with open("key.txt", "r") as file:
    key = file.read()

alphabet = "abcdefghijklmnopqrstuvwxyz"

reverse_key = {}

for i in range(26):
    reverse_key[key[i]] = alphabet[i]

plaintext = ""

for ch in ciphertext:
    if ch in reverse_key:
        plaintext += reverse_key[ch]
    else:
        plaintext += ch

print("Decrypted Text:")
print(plaintext)
