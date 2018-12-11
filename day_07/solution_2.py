with open('input.txt') as file:
    data = file.read()

lines = data.splitlines()

relationships = []

for line in lines:
    first = line.split(" ")[1]
    second = line.split(" ")[7]
    relationships.append((first, second))

order = ""
available_nodes = []
workers = []
num_workers = 5
time = 0
offset = 4 #
final = ''
last_item = True
while len(relationships) > 0:

    # Get a list of parents and children
    parents = set([p[0] for p in relationships])
    children = set([c[1] for c in relationships])

    # Get a list of nodes that have parents that have been processed
    available_nodes = set(a[1] for a in relationships if a[0] in order)

    # Get a list of any nodes that do not have parents that need to be processed and sort them
    head = [node for node in parents if node not in children or node in available_nodes]
    nodes_to_add = [h for h in head if h not in [w[0] for w in workers]]
    nodes_to_add.sort()

    # Add available nodes to any available workers
    while len(workers) < num_workers and len(nodes_to_add) > 0:
        node = nodes_to_add.pop(0)
        workers.append((node, ord(node) - offset + time))

    time += 1

    # Check to see if the workers have processed an item
    for worker in workers:
        if worker[1] <= time:
            order += worker[0]
            workers.remove(worker)

    # If this is the last item, we need to also process the child
    tmp = ''
    if len(relationships) == 1:
        tmp = relationships[0][1]

    # Remove any relationships that has a parent that is in order
    relationships = [relationship for relationship in relationships if relationship[0] not in order]

    # Only process the child once
    if len(relationships) == 0 and last_item:
        relationships.append((tmp,'1'))
        last_item = False



# Add the remaining relationship to order
#order += relationships[0][0]
#order += relationships[0][1]

print("Order of items processed: " + order)
print("Time it took to process: " + str(time))