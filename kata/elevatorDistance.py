# Solution by PauloBA

def elevator_distance(array):
    ac = 0
    h = 0
    for i in array:
        ac = ac + abs(i - h)
        h = i
    ac = ac - array[0]
    return ac

floors = [1, 1]

print(elevator_distance(floors))