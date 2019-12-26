def getT0(plan, vertex):
    T0 = []
    T0.append(0)

    event = 1
    E = []

    while len(T0) != vertex:
        for i in range(0, len(plan)):
            if plan[i][1] == event:
                E.append(T0[plan[i][0]] + plan[i][2])

        maxnum = 0
        for i in range(0, len(E)):
            if maxnum < E[i]:
                maxnum = E[i]

        T0.append(maxnum)
        event += 1
        E.clear()

    return T0
