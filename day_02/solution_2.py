with open('input.txt') as file:
    data = file.read()

box_ids = data.splitlines()

print(''.join([i for i, j in zip([box_id_1 for box_id_1 in box_ids for box_id_2 in box_ids if box_id_1 is not box_id_2 and len([i for i, j in zip(box_id_1, box_id_2) if i == j]) > 24][0], [box_id_1 for box_id_1 in box_ids for box_id_2 in box_ids if box_id_1 is not box_id_2 and len([i for i, j in zip(box_id_1, box_id_2) if i == j]) > 24][1]) if i == j]))
