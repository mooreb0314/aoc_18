with open('input.txt') as file:
    data = file.read()

chars = [c for c in data]

removed = True
while removed:
    removed = False

    for i,_ in enumerate(chars):
        if i < len(chars) - 1:
            if abs(ord(chars[i]) - ord(chars[i+1])) == 32:
                chars.pop(i)
                chars.pop(i)
                removed = True
                break


print(len(chars))