import func

plan = [[0, 1, 8],[0, 2, 10],[0, 3, 4],
        [1, 2, 0],[1, 3, 11],[1, 4, 6],
        [2, 5, 12],[3, 5, 0],[3, 7, 7],
        [4, 5, 8],[4, 7, 4],[5, 6, 8],
        [6, 7, 3]]

vertex = 8
T0 = func.getT0(plan,vertex)
print('T0: ',T0)

S  = func.getS(T0,plan)
print('S: ',S)

T1  = func.getT1(plan,vertex,T0)
print('T1: ',T1)
