import pickle
import numpy as np
with open('player2states','rb') as handle:
    a = pickle.load(handle)
res = np.zeros(64)
res2 = np.zeros(64)
for move, value in a.items():
    if move:
        res[move[1]-1] +=value
        res2[move[1]-1] +=1
res /= res2
print(res.reshape((4,4,4)))