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
                chars.pop(i)
                chars.pop(i)
                removed = True
                break

'''

i = 0
slow = True
#print(chars)
while i < len(chars) - 1:
    #print(str(chars[i]) + " - " +  str(chars[i+1]) +  " = " + str(abs(ord(chars[i]) - ord(chars[i+1]))))

    if abs(ord(chars[i]) - ord(chars[i+1])) == 32:
        #print(chars.pop(i))
        #print(chars.pop(i))
        chars.pop(i)
        chars.pop(i)
        i -= 1
        #print(chars)
    else:
        i += 1




print(''.join(chars))
print(len(chars))