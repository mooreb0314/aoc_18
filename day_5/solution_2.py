with open('input.txt') as file:
    data = file.read()

lower = data.lower()
di = {}
for c in set(lower):
    di[c] = lower.count(c)

print(di)
#print(max(di.keys(), key=(lambda key: di[key])))

#data.replace(max(di.keys(), key=(lambda key: di[key])),"")
#data.replace(max(di.keys(), key=(lambda key: di[key])).upper(),"")

low = 100000
for k in di.keys():
    #print(k)
    tmp = data
    tmp = tmp.replace(k,"")
    tmp = tmp.replace(k.upper(),"")

    chars = [c for c in tmp]
    i = 0

    while i < len(chars) - 1:

        if abs(ord(chars[i]) - ord(chars[i+1])) == 32:
            a = chars.pop(i)
            b = chars.pop(i)

            if i != 0:
                i -= 1

        else:
            i += 1

    if len(chars) < low:
        low = len(chars)

print(low)


