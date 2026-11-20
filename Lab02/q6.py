key = {
    'a':'l', 'b':'u', 'c':'c', 'd':'m', 'e':'o',
    'f':'d', 'g':'g', 'h':'s', 'i':'x', 'j':'q',
    'k':'f', 'l':'r', 'm':'v', 'n':'b', 'o':'a',
    'p':'j', 'q':'n', 'r':'w', 's':'h', 't':'t',
    'u':'z', 'v':'i', 'w':'k', 'x':'p', 'y':'e',
    'z':'y'
}

text = """Cryptography is the art of writing or solving codes.
It has been used for centuries to protect secrets in war,
diplomacy, and private communication."""

text = text.lower()

ciphertext = ""

for ch in text:
    if ch in key:
        ciphertext += key[ch]
    else:
        ciphertext += ch

print("Ciphertext:")
print(ciphertext)