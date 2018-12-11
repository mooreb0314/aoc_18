with open('input.txt') as file:
    data = file.read()

lines = data.splitlines()

relationships = []

for line in lines:
    first = line.split(" ")[1]
    second = line.split(" ")[7]
    relationships.append((first, second))

order = ""
available_children = []
while len(relationships) > 1:
    parents = set([p[0] for p in relationships])
    children = set([c[1] for c in relationships])
    available_children = set(a[1] for a in relationships if a[0] in order)
    head = [node for node in parents if node not in children or node in available_children]
    order += ''.join(sorted(head)[0])
    relationships = [relationship for relationship in relationships if relationship[0] not in order]

# Add the remaining relationship to order
order += relationships[0][0]
order += relationships[0][1]

print(order)