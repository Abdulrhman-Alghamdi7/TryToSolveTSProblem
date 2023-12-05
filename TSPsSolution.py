f = open('33CitiesInfo.csv','r')

l = []
for i in f.readlines():
    l.append((i[:-1]).split(','))
l[-1][-1] = 0

Points = dict()
for i in l[1:]:
    res = {l[0][1:][j]: i[1:][j] for j in range(len(l[1:])) if i[1:][j] != '0'}
    Points[i[0]] = res
for i in Points.keys():
    for j in Points[i].keys():
        Points[i][j] = int(Points[i][j])

def FindMinDis(current, AddedPoint):

    valid_Points = {point: distance for point, distance in current.items() if point not in AddedPoint}
    min_point = min(valid_Points, key=valid_Points.get)
    return min_point, valid_Points[min_point]

road = []
distance = 0
start = 'A'
current = Points[start]
AddedPoint = set()

while len(road) < len(Points):
    if len(road) == 0 and distance == 0:
        road.append(start)
        AddedPoint.add(start)
    next, min_distance = FindMinDis(current, AddedPoint)
    road.append(next)
    AddedPoint.add(next)
    distance += min_distance
    current = Points[next]

road.append(start)
distance += current[start]

print(' -> '.join(road)+'.', f'distance :  {distance}')



