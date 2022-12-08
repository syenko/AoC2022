f = open("inputs/6.txt", "r")

text = ""

for x in f:
    text = x

for i in range(len(text)):
    if len({j for j in text[i:i+14]}) == 14:
        print(i+14)
        break
