with open('input.txt') as file:
    data = file.read()

#data = "dabAcCaCBAcCcaDA"
chars = [c for c in data]

i = 0
while i < len(chars) - 1:

    if abs(ord(chars[i]) - ord(chars[i+1])) == 32:
        a = chars.pop(i)
        b = chars.pop(i)

        if i != 0:
            i -= 1

    else:
        i += 1

print(''.join(chars))
print(len(chars))