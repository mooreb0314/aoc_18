with open('input.txt') as file:
    data = file.read()

lines = data.splitlines()
lines.sort()

guards = []

for line in lines:
    if line.split("] ")[1].startswith("Guard"):
        guard = int(line.split("] ")[1].split(" ")[1].split("#")[1])
        if guard not in guards:
            guards.append(guard)

solution = {"Guard": 0 , "Time" : 0, "Minute": 0}

for guard in guards:
    chosen_guard = guard
    sleeping = False
    time_card = [0 for x in range(60)]

    for line in lines:
        #print(line)
        if line.split("] ")[1].startswith("Guard"):
            curr_guard = int(line.split("] ")[1].split(" ")[1].split("#")[1])
            if curr_guard == chosen_guard:
                i = 1
            else:
                start = 0
                end = 0

        elif int(line.split("] ")[1].startswith("wakes")):
            if curr_guard == chosen_guard:
                #print(line)
                end = int(line.split("] ")[0].split(" ")[1].split(":")[1])
                #print("Start: " + str(start) + " End: " + str(end))
                for i in range(start, end):
                    time_card[i] += 1

                #print(time_card)

        else:

            if curr_guard == chosen_guard:
                #print(line)
                start = int(line.split("] ")[0].split(" ")[1].split(":")[1])

    if max(time_card) > solution["Time"]:
        solution["Guard"] = chosen_guard
        solution["Time"] = max(time_card)
        solution["Minute"] = time_card.index(max(time_card))

print(solution)

print(solution["Guard"] * solution["Minute"])


