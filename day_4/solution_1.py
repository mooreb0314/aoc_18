with open('input.txt') as file:
    data = file.read()

lines = data.splitlines()
lines.sort()

time_card = [0 for x in range(60)]

curr_guard = 0
sleeping = False
start = 0
for line in lines:
    #print(line)
    if line.split("] ")[1].startswith("Guard"):
        curr_guard = int(line.split("] ")[1].split(" ")[1].split("#")[1])
        if curr_guard == 2539:
            print(line)

    elif int(line.split("] ")[1].startswith("wakes")):
        if curr_guard == 2539:
            print(line)
            end = int(line.split("] ")[0].split(" ")[1].split(":")[1])
            print("Start: " + str(start) + " End: " + str(end))
            for i in range(start, end):
                time_card[i] += 1

            print(time_card)

    else:

        if curr_guard == 2539:
            print(line)
            start = int(line.split("] ")[0].split(" ")[1].split(":")[1])

print(time_card.index(max(time_card)))
print(max(time_card))
print((time_card.index(max(time_card))) * 2539)


