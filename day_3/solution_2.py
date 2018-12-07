with open('input.txt') as file:
    data = file.read()

lines = data.splitlines()

# Find all the x and y starting points and the x and y sizes of fabrics
start_x = [int(line.split(' ')[2].split(',')[0]) for line in lines]
start_y = [int(line.split(' ')[2].split(',')[1].split(":")[0]) for line in lines]
range_x = [int(line.split(' ')[3].split('x')[0]) for line in lines]
range_y = [int(line.split(' ')[3].split('x')[1].split(":")[0]) for line in lines]
claims = [int(line.split(' ')[0].split('#')[1]) for line in lines]


# Create fabric that will hold the max possible cut
fabric = [[0 for x in range(max(start_x) + max(range_x))] for y in range(max(start_y) + max(range_y))]


# Lay out the fabric
for line in lines:
    
    coor_x = int(line.split(' ')[2].split(',')[0])
    coor_y = int(line.split(' ')[2].split(',')[1].split(":")[0])
    len_x = int(line.split(' ')[3].split('x')[0])
    len_y = int(line.split(' ')[3].split('x')[1].split(":")[0])
    claim = int(line.split(' ')[0].split('#')[1])

    for x in range(len_x):
        for y in range(len_y):
            if fabric[coor_y + y][coor_x + x] > 0:

                # Remove the past claim from list
                try:
                    claims.remove(fabric[coor_y + y][coor_x + x])
                except ValueError:
                    pass
                
                # Remove the current claim from list
                try:
                    claims.remove(claim)
                except ValueError:
                    continue

            fabric[coor_y + y][coor_x + x] = claim 
        
print(claims[0])

