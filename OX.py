import numpy as np
import random
O = []
X = []
win = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7],
       [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]


def checkWin(P):
    for w in win:
        if all(x-1 in P for x in w):
            return True
    return False


def displayOX():
    OX = np.array([' '] * 9)
    OX[O] = ['O']
    OX[X] = ['X']
    print(OX.reshape([3, 3]))


def calSOX(O, X):
    SO = SX = 0
    criticalmove = []
    for w in win:
        o = [i-1 in O for i in w]
        x = [i-1 in X for i in w]
        if not any(x):
            nO = o.count(True)
            SO += nO
            if nO == 2:
                print('critical', w)
                criticalmove = w
        if not any(o):
            SX += x.count(True)
    return SO, SX, criticalmove


def evalOX(O, X):
    SO, SX, criticalmove = calSOX(O, X)
    return 1 + SX - SO, criticalmove


def AI():
    validmove = list(set(range(9)) - set(O+X))
    V = [-100] * 9
    for m in validmove:
        tempX = X + [m]
        V[m], criticalmove = evalOX(O, tempX)
        if len(criticalmove) > 0:
            move = [i-1 for i in criticalmove if i-1 in validmove]
            return random.choice(move)
    maxV = max(V)
    imaxV = [i for i, j in enumerate(V) if j == maxV]
    return random.choice(imaxV)


while True:
    move = int(input('Choose position [1-9]')) - 1
    while move in O+X or move > 8 or move < 0:
        move = int(input('Bad move : Choose position [1-9]')) - 1
    O.append(move)
    displayOX()
    if checkWin(O):
        print('O Win')
        break
    if len(O) + len(X) == 9:
        print('Draw')
        break
    X.append(AI())
    displayOX()
    if checkWin(X):
        print('X win')
        break
    if len(O) + len(X) == 9:
        print('Draw')
        break
