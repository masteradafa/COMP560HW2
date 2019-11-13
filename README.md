# 3D Tic-Tac-Toe-Reinforcement-learning
We briefly trained an agent to learn how to play 3D tic-tac-toe through reinforcement learning(Q-learning)

<b>Requirements:</b><br />
python 3
pygame

Run <b>Play.py</b> to play game.<br />
```
python Play.py
```
Run <b>Train.py</b> to train the agent. <b>Train.py</b> takes three arguments, which describe the number of trials that should be run to learn. The numbers should be increasing in value. After each number of trials (where each trial is the playing of a full game), the program print out the current utility values for each of the squares to 3 significant digits). For example, to train 100, 200, and 2000 trials.<br />
```
python Train.py 100 200 2000
```

<b>Training:</b><br />
It took a large iterations to master the game since the possible states of this game is very big. A 3 * 3 2D tic-tac-toe has about 3^9 possible states whereas 4 * 4 * 4 3D tic-tac-toe has about 3^64 possible states. The currect states are trained for ~2000 iterations, and the agent is still not very smart. 

currect states can be downloaded via google drive:
player1state: https://drive.google.com/file/d/1oYnqKEp17_Nxtq7ElHYngKolHXc1dDRe/view?usp=sharing
player2state: https://drive.google.com/file/d/1Ld-SyDoCVQ--K3918K5ZI0kXhDogTVzO/view?usp=sharing
