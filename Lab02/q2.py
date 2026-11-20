file = open("PES2UG24CS351.txt", "r")

text = file.read().lower()

print("Frequency:")

words = ["th", "he", "ar", "ing", "e", "or"]

for word in words:
    print(word, "=", text.count(word))

file.close()