 x = input()
    valores = x.split()

    dq = deque()

    for i in range(len(valores)):
        dq.append(valores[i])