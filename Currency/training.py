from typing import Dict
import string

string1 = "asfgglqeibgqjnkqeavroigejggqeq'3ot482hgo4pgqwr"

d: Dict[str, int] = {}

for letter in string1:
    if letter in d:
        d[letter] = d[letter] + 1
    else:
        d[letter] = 1
for key, value in d.items():
    print("key: ", key, " value: ",value)

word = "lsslsl"
word[0] = 'a'
print(word)