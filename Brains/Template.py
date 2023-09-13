class Brain:
    def __init__(self):
        self.name = "My awesome brain name"
        self.gameState = None
    
    def updateGameState(self, gameState):
        self.gameState = gameState
    
    def chooseMove(self):
        # return type is string
        # return value must be one of "cards", "trains", "tickets"
        return "tickets"
    
    def chooseCard(self, drawPile, previousChoice):
        # return value must be a value in drawPile or "draw_pile"
        # previousChoice is None on first choice. 
        pass
    
    def chooseRoute(self):
        # return a tuple of three elements.
        # 1. a list containing two cities
        # 2. a string representing the color of the route
        # 3. an integer representing the number of wild cards used
        pass

    def chooseTickets(self, tickets):
        # return a sublist of tickets. The list must have length larger than or equal to 1
        return tickets
    
