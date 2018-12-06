with open('input.txt') as file:
    data = file.read()

box_ids = data.splitlines()

test_1 = ["abcdef","bababc","abbcde","abcccd","aabcdd","abcdee","ababab"]

#box_ids = test_1
total_freq = {'2':0, '3':0}
for box_id  in box_ids:
    freq = {}
    count_3 = True
    count_2 = True
    for letter in box_id:
        if letter in freq.keys():
            freq[letter] += 1
        else:
            freq[letter] = 1

    for key in freq.keys():
        if freq[key] == 3 and count_3:
            count_3 = False            
            total_freq['3'] +=1
        if freq[key] == 2 and count_2:
            count_2 = False
            total_freq['2'] +=1


print(total_freq['2'] * total_freq['3'])