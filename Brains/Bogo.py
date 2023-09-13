import numpy as np
import TTRConstants as constants

class Brain:
    def __init__(self):
        self.name = "My awesome brain name"
        self.gameState = None
    
    def updateGameState(self, gameState):
        self.gameState = gameState
    
    def chooseMove(self):
        # return type is string
        # return value must be one of "cards", "trains", "tickets"
        return np.random.choice(["cards","trains","tickets"]) 
    
    def chooseCard(self, drawPile, previousChoice):
        # return value must be a value in drawPile or "draw_pile"
        # previousChoice is None on first choice. 
        return "draw_pile"
    
    def chooseRoute(self):
        # return a tuple of three elements.
        # 1. a list containing two cities
        # 2. a string representing the color of the route
        # 3. an integer representing the number of wild cards used
        edge=constants.edges[np.random.randint(0,20)]
        cities=list(edge[0:2])
        color=np.random.choice(constants.possibleColors)
        wilds=np.random.randint(0,2)
        print(cities)
        return (cities,color,wilds)

    def chooseTickets(self, tickets):
        # return a sublist of tickets. The list must have length larger than or equal to 1
        return [tickets[1],tickets[2]]
    