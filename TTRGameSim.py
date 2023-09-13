
#this version no longer takes input from user. 
#Designed for computer OR human player (mainly comp v comp sim)

#All values and methods associated with the Original Ticket to Ride board game
import TTRBoard
import TTRCards
import TTRPlayer
import collections
import pprint
import importlib
import os

class Game(object):
    def __init__(self, numPlayers):
        
        self.sizeDrawPile          = 5
        self.numTicketsDealt       = 3
        self.sizeStartingHand      = 4
        self.maxWilds              = 3

        self.endingTrainCount      = 3 # ending condition to trigger final round

        self.pointsForLongestRoute = 10
        self.startingNumOfTrains   = 45 #45
        self.deck                  = TTRCards.Cards(self.sizeDrawPile, self.maxWilds)
        
        self.board                 = TTRBoard.Board()
        self.numPlayers            = numPlayers
        self.players               = []

        self.turns = []
        
        self.posToMove             = 0
    

        #point values for tracks of different lengths
        self.routeValues           = {1:1, 2:2, 3:4, 4:7, 5:10, 6:15}

        #Here we import the brains

        file_names=[file_name[:-3] for file_name in os.listdir("./Brains") if file_name.endswith('.py')]


        for position in range(numPlayers):
            startingHand     = self.deck.dealCards(self.sizeStartingHand)
            startingTickets  = []
            playerBoard      = TTRBoard.PlayerBoard()
            #Here we


            player           = TTRPlayer.Player(startingHand, 
                                                startingTickets, 
                                                playerBoard, 
                                                position, 
                                                self.startingNumOfTrains,
                                                importlib.import_module("Brains." + file_names[position])
                                                )                          
            self.players.append(player)

    def getOpenInfo(self, player):
        """returns a dict of open info for all players
        """
        openInfo = {
            'graph': self.board.G,
            'hand': player.hand,
            'discard': self.deck.discardPile,
            'trains': {p : self.players[p].getNumTrains() for p in range(self.numPlayers)},
            # 'draw_pile': self.deck.getAvailableCards(),
            'hand_sizes': {p : len(self.players[p].hand) for p in range(self.numPlayers)},
            'num_tickets': {p : len(self.players[p].getTickets()) for p in range(self.numPlayers)},
            # 'scores' : {p : self.players[p].getScore() for p in range(self.numPlayers)},
            'turns': self.turns
        }
        
        return openInfo
    
    def printSepLine(self, toPrint):
        print (toPrint)
            
    def advanceOnePlayer(self):
        """Updates self.posToMove"""
        self.posToMove += 1
        self.posToMove %= self.numPlayers
    
    def getCurrentPlayer(self):
        return self.players[self.posToMove]
    
    def doesPlayerHaveCardsForEdge(self, player, chosen_edge, wild_count):
        routeDist = chosen_edge.weight
        routeColor = chosen_edge.color
        if wild_count >= player.hand['wild']:
            return False
        elif player.hand(routeColor) + wild_count >= routeDist:
            return True
        return False      
    
    def checkEndingCondition(self, player):
        return player.getNumTrains() < self.endingTrainCount
    
    def initialize(self):
        """Before game turns starts, enter names and pick destination tickets
        """
        
        for player in self.players:
                
            #pick desination tickets
            
            self.pickTickets(player)
            
            self.advanceOnePlayer()

    def scorePlayerTickets(self, player):
        """returns None.  
        Scores player's destination tickets and 
        adds/subtracts from player's points
        """
        for ticket in player.tickets:
            city1 = ticket[0]
            city2 = ticket[1]
            value = ticket[2]
            posNodes = player.playerBoard.getNodes()
            if city1 not in posNodes or city2 not in posNodes:
                player.subtractPoints(value)
                continue
            if player.playerBoard.hasPath(city1, city2):
                player.addPoints(value)
                
    def scoreLongestPath(self):
        """determines which player has the longest route and 
        adjusts their score accordingly
        players: list of players
        adds self.pointsForLongestRoute to player with longest route
        """

        scores = { x:(0, ()) for x in self.players }
        longestPath = 0
        for player in scores:

            for city in player.playerBoard.getCities():
                pathInfo = player.playerBoard.longestPath(city)
                if pathInfo[0] > scores[player][0]:
                    scores[player] = pathInfo
        
            if scores[player][0] > longestPath:
                longestPath = scores[player][0]
        
        print (scores)
        
        for player in scores:
            if scores[player][0] == longestPath:
                player.addPoints(self.pointsForLongestRoute)
        
        #does not return anthing

    def printAllPlayerData(self):
        """prints out all of the non method attributes values for all players
        """
        for player in self.players:
            print (player.name)
            print ("------------------------------")
            for x in player.__dict__:
                print (x, player.__dict__[x])
                    
            print ("==============================")

    def playTurn(self, player):
        """player chooses 'cards', 'trains', 'tickets'
        player: player object
        """
        player.brain.updateGameState(self.getOpenInfo(player))
        choice = player.brain.chooseMove()

        if choice not in ['cards', 'trains', 'tickets']:
            return {
                "action" : None,
                "result" : None
            }


        #displayMap = input("Display map? y/n: ")
        #if displayMap == 'y':
        #    pauseTime = input("For how many seconds? (between 1 and 30): ")
        #    if int(pauseTime) not in range(1, 31):
        #        pass
        #    else:
        #        self.board.showBoard(self.board.G, int(pauseTime))
        #        #Depricated?
        
        actions = {
            "cards" : self.pickCards,
            "trains" : self.placeTrains,
            "tickets" : self.pickTickets
        }
        result = actions[choice](player)

        return {
            "action" : choice,
            "result" : result
        }
    
    def pickCards(self, player):
        
        choice1 = player.brain.chooseCard(self.deck.getDrawPile(),None)

        if choice1 not in (self.deck.getDrawPile() + ['draw_pile']):
               return None
        
        #add card to player's hand
        #remove it from drawPile or cards and 
        #add new card to drawPile
        if choice1 == 'draw_pile':
            chosenCard1 = self.deck.pickFaceDown()
            player.addCardToHand(chosenCard1)
        else:
            player.addCardToHand(self.deck.pickFaceUpCard(choice1))
        
        #start second card selection
        if choice1 == 'wild':
            return {'chosen': [choice1]}
        
         
        choice2 = player.brain.chooseCard(self.deck.getDrawPile(), choice1)
        if choice2 == 'wild'  \
               or (choice2 not in self.deck.getDrawPile() + ['draw_pile']):
            return None
            
        #add card to player's hand
        #remove it from drawPile or cards and 
        #add new card to drawPile
        if choice2 == 'draw_pile':
            chosenCard = self.deck.pickFaceDown()
            player.addCardToHand(chosenCard)
        else:
            player.addCardToHand(self.deck.pickFaceUpCard(choice2))
        
        return {
            'chosen' : [choice1, choice2]
        }
    
    def placeTrains(self, player):
        
        route,build_color,wild_count = player.brain.chooseRoute()
        
        edges=self.board.G.edges(route[0],route[1],keys=True,data=True)
        edges=[edge for edge in edges if edge[-1]["owner"]==None]
    
        if len(edges)==0:
            return None
    
        chosen_edge=[]
        for edge in edges:
            if edge.color == 'grey':
                chosen_edge=edge
                break
            elif edge.color == build_color:
                chosen_edge=edge
                break
            else:
                return None



        if not self.doesPlayerHaveCardsForEdge(player, chosen_edge,wild_count):
            return None

    
        #remove cards from player's hand
        player.removeCardsFromHand('wild', wild_count)
        player.removeCardsFromHand(build_color, chosen_edge.weight - wild_count)

        #claim route for player (see dedicated method within Game class)
        chosen_edge.owner=player.position
        player.playerBoard.addEdge(chosen_edge)

        #calculate points
        player.addPoints(self.routeValues[chosen_edge.weight])
        
        #add cards to discard pile
        self.deck.addToDiscard(build_color * (chosen_edge.weight - wild_count) + ['wild']*wild_count)
        
        #remove trains from players numTrains
        player.playNumTrains(chosen_edge.weight)  

        return {
            "route" : route,
            "color" : build_color,
            "wilds" : wild_count
        }
    
    def pickTickets(self, player, minkeep = 1):
        tickets = self.deck.dealTickets(self.numTicketsDealt)        
        chosenTickets = player.brain.chooseTickets(tickets)
        # check if player has chosen enough tickets
        if len(chosenTickets) < minkeep and len(tickets) > 0:
            chosenTickets = tickets[0:minkeep]

        for ticket in chosenTickets:
            player.addTicket(ticket)
        
        
        #add tickets that weren't chosen to the ticketDiscardPile
        notChosen = list(set(tickets).difference(chosenTickets))
        print(notChosen)
        self.deck.replaceTicketCards(notChosen)
#        for i in notChosen:
 #           self.deck.addToTicketDiscard(tickets[i])        
        
        return {
            "num_tickets": len(chosenTickets)
        }
    

def playTTR(numPlayers):
    
    game = Game(int(numPlayers))    
    
    game.initialize()
    
    player = game.players[game.posToMove]



    #main game loop
    while True:
        result = game.playTurn(player)
        game.turns.append(result)
        
        #condition to break out of loop
        if game.checkEndingCondition(player):
            game.advanceOnePlayer()
            player = game.getCurrentPlayer()
            break
        game.advanceOnePlayer()
        player = game.getCurrentPlayer()
    
    print ("\n This is the last round!  Everyone has one more turn! \n")
    
    for i in range(len(game.players)):
        print ("\n_________________NEW PLAYER'S TURN_________________ \n")
        print ("This is your LAST TURN " + str(player.getName()) + "! ")
        game.playTurn(player)
        game.advanceOnePlayer()
        player = game.getCurrentPlayer()
    
    
    for player in game.players:
        game.scorePlayerTickets(player)
    
    game.scoreLongestPath()
    

    scores = []
    for player in game.players:
        print ((str(player.getName()) )
               + " had " 
               + str(player.getPoints()) 
               + " points!"
               )
        score = player.getPoints()
        scores.append(score)
        
    
    winners = [x.getName() for x in game.players 
              if x.getPoints() == max(scores)]

    if len(winners) == 1:
        print ("The winner is " + str(winners[0]))
    else:
        print ("The winners are " + ' and '.join(winners))
    
    
    print ("\n =========== Data =========== \n")
    
    game.printAllPlayerData()
    
    print ("\n =========== fin =========== \n")

if __name__ == "__main__":

    playTTR()

