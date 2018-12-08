with open('input.txt') as file:
    data = file.read()

#data = "dabAcCaCBAcCcaDA"
chars = [c for c in data]

'''
removed = True
while removed:
    removed = False

    for i,_ in enumerate(chars):
        if i < len(chars) - 1:
            if abs(ord(chars[i]) - ord(chars[i+1])) == 32:
                a = chars.pop(i)
                b = chars.pop(i)
                print("Removed: " + a + b)
                removed = True
                break

'''

i = 0
#print(chars)
while i < len(chars) - 1:
    #print(str(chars[i]) + " - " +  str(chars[i+1]) +  " = " + str(abs(ord(chars[i]) - ord(chars[i+1]))))
    #print(chars[-10:])

    if abs(ord(chars[i]) - ord(chars[i+1])) == 32:
        #print(chars.pop(i))
        #print(chars.pop(i))
        a = chars.pop(i)
        b = chars.pop(i)
        #print("Removed: " + a + b)
        if i != 0:
            i -= 1
        #print(chars)
    else:
        i += 1



print(''.join(chars))
print(len(chars))