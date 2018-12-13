with open('input.txt') as file:
    data = file.read()

license_file = [int(n) for n in data.split(" ")]

# h = header
# c = child node
# m = metadata
switch = "h"
metadata = []
nodes = []
total = 0
for d in license_file:
    print("Switch: " + switch + " item: " + str(d))
    if switch == "h":
        # At header, getting num child nodes
        if len(nodes) > 0:
            nodes[-1] -= 1
        nodes.append(d)
        switch = 'c'
    elif switch == "c":
        # Metadata for child node
        metadata.append(d)

        if nodes[-1] > 0:
            switch = 'h'
        else:
            switch = 'm'
    else:
        # Metadata
        total += d
        metadata[-1] -= 1

        # If we are done processing metadata for this node, it is either more meta data or a header
        if metadata[-1] == 0:
            metadata.pop()

            # If there are more nodes at this level we must be at another header
            if nodes[-1] > 0:
                switch = 'h'
                nodes[-1] -= 1
            # Else, there are no more nodes, and we have to see if we are at more meta data (0 in previous index) more header( >0 in previous index)
            else:

                # Remove last node and look to see if we are at a header
                nodes.pop()
                if len(nodes) > 0:
                    # If we are here, we must be at another header
                    if nodes[-1] > 0:
                        switch = 'h'
                    # Else, this means we can process more metadata
                    else:
                        switch = 'm' # shouldn't actually change anything can be removed




    print("Metadata Array: " + str(metadata))
    print("Nodes Array: " + str(nodes))

print(total)
