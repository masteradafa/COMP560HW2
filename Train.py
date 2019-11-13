from Game import TicTacToe
from QLearning import  Qlearning
import sys

ites = []
assert len(sys.argv)-1==3
for i in range(1,4):
    ites.append(int(sys.argv[i]))
game = TicTacToe(True) #game instance, True means training
player1= Qlearning() #player1 learning agent
player2 =Qlearning() #player2 learning agent
game.startTraining(player1,player2)
game.train(ites[2],ites)
game.saveStates() 
