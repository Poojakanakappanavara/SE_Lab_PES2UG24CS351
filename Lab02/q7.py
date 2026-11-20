from collections import Counter

ciphertext = """BFPXTRWTOW CEN BRTEWTA JNFVU E NJLNWFWJWFGV BFPXTR CXTRT TEBX QTWWTR MEPN WG
EVGWXTR VGWFBT WXT PEWWTRV GZ WXT CGRAN WXT BGMMGV QTWWTRN GZ WXT TVUQFNX
EQPXELTW XTQP FV ATBGAFVU E NMEQQ UJTNN EW ZFRNW WTNWFVU WXTM FV WXT WTOW
EVA WXT RTNJQW LTBGMTN BQTERTR WXT PRGBTNN RTDTEQN WXT NTBRTW GZ WXT BGAT GVBT
WXT MEPPFVU FN BGRRTBW WXT MTNNEUT XFAATV FN WXEW NJLNWFWJWFGV BFPXTRN ERT
NFMPQT LJW ZRTIJTVBK EVEQKNFN MESTN WXTM CTES"""

ciphertext = ciphertext.upper()

letters = [ch for ch in ciphertext if ch.isalpha()]

frequency = Counter(letters)

total = len(letters)

print("Letter Frequency Table")
print("----------------------")

for letter in sorted(frequency):
    count = frequency[letter]
    percentage = (count / total) * 100
    print(letter, count, round(percentage, 2))

print("----------------------")
print("Total letters =", total)


key = {
    'A':'d', 'B':'c', 'C':'w', 'D':'v', 'E':'a',
    'F':'i', 'G':'o', 'I':'q', 'J':'u', 'K':'y',
    'L':'b', 'M':'m', 'N':'s', 'O':'x', 'P':'p',
    'Q':'l', 'R':'r', 'S':'k', 'T':'e', 'U':'g',
    'V':'n', 'W':'t', 'X':'h', 'Z':'f'
}

plaintext = ""

for ch in ciphertext:
    if ch in key:
        plaintext += key[ch]
    else:
        plaintext += ch

print("\nDecrypted Plaintext:")
print(plaintext)

