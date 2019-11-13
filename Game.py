import pygame
import random
import time
from QLearning import Qlearning

#human player
class Humanplayer:
    pass

#randomplayer player
class Randomplayer:
    def __init__(self):
        pass
    def move(self,possiblemoves):
        return random.choice(possiblemoves)

class TicTacToe:
    def __init__(self,training=False):
        self.board = [' ']*64

        self.done = False
        self.human=None
        self.computer=None
        self.humanTurn=None
        self.training=training
        self.player1 = None
        self.player2 = None
        self.aiplayer=None
        self.isAI=False
        # if not training display
        if(not self.training):
            pygame.init()
            self.ttt = pygame.display.set_mode((200,800))
            pygame.display.set_caption('Tic-Tac-Toe')
            

    #reset the game
    def reset(self):
        if(self.training):
            self.board = [' '] * 64
            return

        self.board = [' '] * 64
        self.humanTurn=random.choice([True,False])

        self.surface = pygame.Surface(self.ttt.get_size())
        self.surface = self.surface.convert()
        self.surface.fill((250, 250, 250))

        # veritical line
        pygame.draw.line(self.surface, (0, 0, 0), (50, 0), (50, 800), 2)
        pygame.draw.line(self.surface, (0, 0, 0), (100, 0), (100, 800), 2)
        pygame.draw.line(self.surface, (0, 0, 0), (150, 0), (150, 800), 2)
        # horitical line
        pygame.draw.line(self.surface, (0, 0, 0), (0,50), (200, 50), 2)
        pygame.draw.line(self.surface, (0, 0, 0), (0,100), (200, 100), 2)
        pygame.draw.line(self.surface, (0, 0, 0), (0,150), (200, 150), 2)
        pygame.draw.line(self.surface, (0, 0, 0), (0,200), (200, 200), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (0,250), (200, 250), 2)
        pygame.draw.line(self.surface, (0, 0, 0), (0,300), (200, 300), 2)
        pygame.draw.line(self.surface, (0, 0, 0), (0,350), (200, 350), 2)
        pygame.draw.line(self.surface, (0, 0, 0), (0,400), (200, 400), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (0,450), (200, 450), 2)
        pygame.draw.line(self.surface, (0, 0, 0), (0,500), (200, 500), 2)
        pygame.draw.line(self.surface, (0, 0, 0), (0,550), (200, 550), 2)
        pygame.draw.line(self.surface, (0, 0, 0), (0,600), (200, 600), 5)
        pygame.draw.line(self.surface, (0, 0, 0), (0,650), (200, 650), 2)
        pygame.draw.line(self.surface, (0, 0, 0), (0,700), (200, 700), 2)
        pygame.draw.line(self.surface, (0, 0, 0), (0,750), (200, 750), 2)
        pygame.draw.line(self.surface, (0, 0, 0), (0,800), (200, 800), 2)
    def evaluate(self, ch):
    
        #over the first dim (vertical layer facing front)
        for j in range(0,64,16):
            # "rows checking"
            for i in range(4):
                if (ch == self.board[i * 4 + j] == self.board[i * 4 + j + 1] and self.board[i * 4 + j + 1] == self.board[i * 4 + j + 2] and self.board[i * 4 + j + 2] == self.board[i * 4 + j + 3]):
                    return 1.0, True
            # "col checking"
            for i in range(4):
                if (ch == self.board[i+j+0] == self.board[i+j+4] and self.board[i+j+4] == self.board[i+j+8] and self.board[i+j+8] == self.board[i+j+12]):
                    return 1.0, True
            # diagonal checking
            if (ch == self.board[0+j] == self.board[5+j] and self.board[5+j] == self.board[10+j] and self.board[10+j] == self.board[15+j]):
                return 1.0, True

            if (ch == self.board[3+j] == self.board[6+j] and self.board[9+j] == self.board[6+j] and self.board[9+j] == self.board[12+j]):
                return 1.0, True

        #over the second dim (horizontal layer)
        for j in range(0,16,4):
            # "rows checking": same as previous dim
            # "col checking"
            for i in range(4):
                if (ch == self.board[i+j+0] == self.board[i+j+16] and self.board[i+j+16] == self.board[i+j+32] and self.board[i+j+32] == self.board[i+j+48]):
                    return 1.0, True
            # diagonal checking
            if (ch == self.board[0+j] == self.board[17+j] and self.board[17+j] == self.board[34+j] and self.board[34+j] == self.board[51+j]):
                return 1.0, True
            if (ch == self.board[3+j] == self.board[18+j] and self.board[33+j] == self.board[18+j] and self.board[33+j] == self.board[48+j]):
                return 1.0, True
        
        for j in range(4):
            # "rows checking"
            for i in range(0,16,4):
                if (ch == self.board[i + j] == self.board[i + j + 16] and self.board[i + j + 16] == self.board[i + j + 32] and self.board[i + j + 32] == self.board[i + j + 48]):
                    return 1.0, True
            # diagonal checking
            if (ch == self.board[0+j] == self.board[20+j] and self.board[20+j] == self.board[40+j] and self.board[40+j] == self.board[60+j]):
                return 1.0, True
            if (ch == self.board[48+j] == self.board[36+j] and self.board[36+j] == self.board[24+j] and self.board[24+j] == self.board[12+j]):
                return 1.0, True

        #cross all dim
        if (ch == self.board[0] == self.board[21] and self.board[21] == self.board[42] and self.board[42] == self.board[63]):
                return 1.0, True
        if (ch == self.board[3] == self.board[22] and self.board[22] == self.board[41] and self.board[41] == self.board[60]):
                return 1.0, True
        if (ch == self.board[12] == self.board[25] and self.board[25] == self.board[38] and self.board[38] == self.board[51]):
                return 1.0, True
        if (ch == self.board[15] == self.board[26] and self.board[26] == self.board[37] and self.board[37] == self.board[48]):
                return 1.0, True

        # "if filled draw"
        if not any(c == ' ' for c in self.board):
            return 0.5, True

        return 0.0, False

    #return remaining possible moves
    def possible_moves(self):
        return [moves + 1 for moves, v in enumerate(self.board) if v == ' ']

    #take next step and return reward
    def step(self, isX, move):
        if(isX):
            ch = 'X'
        else:
            ch = '0'
        if(self.board[move-1]!=' '): # try to over write
            return  -5, True

        self.board[move-1]= ch
        reward,done = self.evaluate(ch)
        return reward, done


    #draw move on window
    def drawMove(self, pos,isX):
        #pos: 1-64
        row=int((pos-1)/4)
        col=(pos-1)%4

        centerX = ((col) * 50) + 20
        centerY = ((row) * 50) + 20

        reward, done= self.step(isX,pos) #next step
        if(reward==-5): #overlap
            return reward, done

        if (isX): #playerX
            font = pygame.font.Font(None, 24)
            text = font.render('X', 1, (10, 10, 10))
            self.surface.blit(text, (centerX, centerY))
            self.board[pos-1] ='X'

            if(self.human and reward==1):
                print('Human won!')

            elif (self.computer and reward == 1):
                print('computer won!')
        else:  #playerO 
            font = pygame.font.Font(None, 24)
            text = font.render('O', 1, (10, 10, 10))
            self.surface.blit(text, (centerX, centerY))
            self.board[pos-1] = '0'

            if (not self.human and reward == 1):  
                print('Human won!')

            elif (not self.computer and reward == 1): 
                print('computer won!')

        if (reward == 0.5):  # draw
            print('Draw Game!')
            return reward, done

        return reward,done

    def mouseClick(self):
        #locating mouse click on board
        (mouseX, mouseY) = pygame.mouse.get_pos()
        if (mouseY < 50): row = 0
        elif (mouseY < 100): row = 1
        elif (mouseY < 150): row = 2
        elif (mouseY < 200): row = 3
        elif (mouseY < 250): row = 4
        elif (mouseY < 300): row = 5
        elif (mouseY < 350): row = 6
        elif (mouseY < 400): row = 7
        elif (mouseY < 450): row = 8
        elif (mouseY < 500): row = 9
        elif (mouseY < 550): row = 10
        elif (mouseY < 600): row = 11
        elif (mouseY < 650): row = 12
        elif (mouseY < 700): row = 13
        elif (mouseY < 750): row = 14
        else:
            row = 15

        if (mouseX < 50): col = 0
        elif (mouseX < 100):col = 1
        elif (mouseX < 150):col = 2
        else: col = 3

        return row * 4 + col + 1

    #update state
    def updateState(self,isX):
        pos=self.mouseClick()
        reward,done = self.drawMove(pos,isX)
        return reward, done

    #show display
    def showboard(self):
        self.ttt.blit(self.surface, (0, 0))
        pygame.display.flip()

    #begin training
    def startTraining(self,player1,player2):
        if(isinstance(player1,Qlearning) and isinstance(player2, Qlearning)):
            self.training = True
            self.player1=player1
            self.player2=player2

    #tarin function
    def train(self,iterations,*argv):
        #*argv are three arguments of trial numbers to display
        ites = []
        for arg in argv[0]:
            ites.append(arg)
        print(ites)
        if(self.training):
            for i in range(iterations+1):
                display = False
                if i in ites:
                    display = True
                if display:
                    print("trainining", i, "display",display)
                self.player1.game_begin()
                self.player2.game_begin()
                self.reset()
                done = False
                isX = random.choice([True, False])
                while not done:
                    if isX:
                        move = self.player1.epslion_greedy(self.board, self.possible_moves(),display)
                    else:
                        move = self.player2.epslion_greedy(self.board, self.possible_moves(),display)

                    reward, done = self.step(isX, move)

                    if (reward == 1):  # won
                        if (isX):
                            self.player1.updateQ(reward, self.board, self.possible_moves())
                            self.player2.updateQ(-1 * reward, self.board, self.possible_moves())
                        else:
                            self.player1.updateQ(-1 * reward, self.board, self.possible_moves())
                            self.player2.updateQ(reward, self.board, self.possible_moves())

                    elif (reward == 0.5):  # draw
                        self.player1.updateQ(reward, self.board, self.possible_moves())
                        self.player2.updateQ(reward, self.board, self.possible_moves())

                    elif (reward == -5):  # illegal move
                        if (isX):
                            self.player1.updateQ(reward, self.board, self.possible_moves())
                        else:
                            self.player2.updateQ(reward, self.board, self.possible_moves())

                    elif (reward == 0): # lose
                        if (isX):  # update opposite
                            self.player2.updateQ(reward, self.board, self.possible_moves())
                        else:
                            self.player1.updateQ(reward, self.board, self.possible_moves())

                    isX = not isX  #change turn

    #save Qtables
    def saveStates(self):
        self.player1.saveQtable("player1states")
        self.player2.saveQtable("player2states")

    #start game human vs AI or human vs random
    def startGame(self, playerX, playerO):
        if (isinstance(playerX, Humanplayer)):
            self.human, self.computer = True, False
            if (isinstance(playerO, Qlearning)): #if AI
                self.ai = playerO
                self.ai.loadQtable("player2states") 
                self.ai.epsilon = 0 #set eps to 0 so always choose greedy step
                self.isAI = True
            elif (isinstance(playerO, Randomplayer)): #if random
                self.ai = playerO
                self.isAI = False

        elif (isinstance(playerO, Humanplayer)):
            self.human, self.computer = False, True
            if (isinstance(playerX, Qlearning)): #if AI
                self.ai = playerX
                self.ai.loadQtable("player1states") 
                self.ai.epsilon = 0 #set eps to 0 so always choose greedy step
                self.isAI = True
            elif(isinstance(playerX, Randomplayer)):#if random
                self.ai=playerX
                self.isAI = False

    def render(self):
        running = 1
        done = False
        pygame.event.clear()
        while (running == 1):
            if (self.humanTurn): #human click
                print("Human player turn")
                event = pygame.event.wait()
                while event.type != pygame.MOUSEBUTTONDOWN:
                    event = pygame.event.wait()
                    self.showboard()
                    if event.type == pygame.QUIT:
                        running = 0
                        print("pressed quit")
                        break

                _, done = self.updateState(self.human) #if random
                self.showboard()
                if (done): #if done reset
                    time.sleep(1)
                    self.reset()
            else:  #AI or random turn
                if(self.isAI):
                    moves = self.ai.epslion_greedy(self.board, self.possible_moves(),False)
                    _, done = self.drawMove(moves, self.computer)
                    print("computer's AI player turn")
                    self.showboard()
                else: #random player
                    moves = self.ai.move(self.possible_moves()) #random player
                    _, done = self.drawMove(moves, self.computer)
                    print("computer's random player turn")
                    self.showboard()

                if (done): #if done reset
                    time.sleep(1)
                    self.reset()

            self.humanTurn = not self.humanTurn




