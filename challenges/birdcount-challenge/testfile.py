bird_list = [{'name': 'mus', 'key': 'm', 'count': 0},
             {'name': 'duif', 'key': 'd', 'count': 0},
             {'name': 'koolmees', 'key': 'k', 'count': 0},
             {'name': 'kraai', 'key': 'i', 'count': 0},
             ]

print('Bird counter until dot')
# TO DO:

# 1) print all birds with key and name

# In this code it will Loop through each bird in the bird_list, print its key and name
for bird in bird_list:
    print(f"{bird['key']}: {bird['name']}")

