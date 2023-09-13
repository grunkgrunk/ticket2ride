

sizeDrawPile          = 5
numTicketsDealt       = 3
sizeStartingHand      = 4
maxWilds              = 3

endingTrainCount      = 3 # ending condition to trigger final round

pointsForLongestRoute = 10
startingNumOfTrains   = 45

routeValues           = {1:1, 2:2, 3:4, 4:7, 5:10, 6:15}

cities = ['Atlanta',        'Boston',         'Calgary',
                        'Charleston',    'Chicago',        'Dallas',     
                        'Denver',        'Duluth',         'El Paso',
                        'Helena',        'Houston',        'Kansas City', 
                        'Las Vegas',     'Little Rock',    'Los Angeles', 
                        'Miami',         'Montreal',       'Nashville',
                        'New Orleans',   'New York',       'Oklahoma City',
                        'Omaha',         'Phoenix',        'Pittsburgh',
                        'Portland',      'Raleigh',        'Saint Louis', 
                        'Salt Lake City','San Francisco',  'Santa Fe',
                        'Sault St Marie','Seattle',        'Toronto', 
                        'Vancouver',     'Washington',     'Winnipeg'
                        ]



tickets = [('Los Angeles',    'New York City', 21), 
                        ('Duluth',         'Houston',        8), 
                        ('Sault St Marie', 'Nashville',      8), 
                        ('New York',       'Atlanta',        6), 
                        ('Portland',       'Nashville',     17), 
                        ('Vancouver',      'Montreal',      20), 
                        ('Duluth',         'El Paso',       10), 
                        ('Toronto',        'Miami',         10), 
                        ('Portland',       'Phoenix',       11), 
                        ('Dallas',         'New York City', 11), 
                        ('Calgary',        'Salt Lake City', 7), 
                        ('Calgary',        'Phoenix',       13), 
                        ('Los Angeles',    'Miami',         20), 
                        ('Winnipeg',       'Little Rock',   11), 
                        ('San Francisco',  'Atlanta',       17), 
                        ('Kansas City',    'Houston',        5), 
                        ('Los Angeles',    'Chicago',       16), 
                        ('Denver',         'Pittsburgh',    11), 
                        ('Chicago',        'Santa Fe',       9), 
                        ('Vancouver',      'Santa Fe',      13), 
                        ('Boston',         'Miami',         12), 
                        ('Chicago',        'New Orleans',    7), 
                        ('Montreal',       'Atlanta',        9), 
                        ('Seattle',        'New York',      22), 
                        ('Denver',         'El Paso',        4), 
                        ('Helena',         'Los Angeles',    8), 
                        ('Winnipeg',       'Houston',       12), 
                        ('Montreal',       'New Orleans',   13), 
                        ('Sault St Marie', 'Oklahoma City',  9),
                        ('Seattle',        'Los Angeles',    9)
                        ]

possibleColors = ["red",   "orange", "yellow", 
                    "green", "blue",   "purple", 
                    "white", "black"
                    ]

numberColors = 12
numberWilds  = 14

edges = [
            ('Los Angeles', 'San Francisco', 3, ['yellow', 'purple']),
            ('Los Angeles', 'Las Vegas', 2, ['grey']),
            ('Los Angeles', 'Phoenix', 3, ['grey']),
            ('Las Vegas', 'Salt Lake City', 3, ['orange']),
            ('Salt Lake City', 'Helena', 3, ['purple']),
            ('Helena', 'Winnipeg', 4, ['blue']),
            ('Helena', 'Denver', 4, ['green']),
            ('Salt Lake City', 'Denver', 3, ['red', 'yellow']),
            ('Phoenix', 'Santa Fe', 3, ['grey']),
            ('Los Angeles', 'El Paso', 6, ['black']),
            ('Phoenix', 'El Paso', 3, ['grey']),
            ('El Paso', 'Santa Fe', 2, ['grey']),
            ('Santa Fe', 'Denver', 2, ['grey']),
            ('Helena', 'Duluth', 6, ['orange']),
            ('Helena', 'Omaha', 5, ['red']),
            ('Winnipeg', 'Duluth', 4, ['black']),
            ('Winnipeg', 'Sault St Marie', 6, ['grey']),
            ('Denver', 'Omaha', 4, ['purple']),
            ('Denver', 'Kansas City', 4, ['black', 'orange']),
            ('Denver', 'Oklahoma City', 4, ['red']),
            ('Santa Fe', 'Oklahoma City', 3, ['blue']),
            ('El Paso', 'Oklahoma City', 5, ['yellow']),
            ('El Paso', 'Dallas', 4, ['red']),
            ('El Paso', 'Houston', 6, ['green']),
            ('Houston', 'Dallas', 1, ['grey', 'grey']),
            ('Dallas', 'Oklahoma City', 2, ['grey', 'grey']),
            ('Oklahoma City', 'Kansas City', 2, ['grey', 'grey']),
            ('Omaha', 'Kansas City', 1, ['grey', 'grey']),
            ('Omaha', 'Duluth', 2, ['grey', 'grey']),
            ('Duluth', 'Sault St Marie', 3, ['grey']),
            ('Duluth', 'Toronto', 6, ['purple']),
            ('Duluth', 'Chicago', 3, ['red']),
            ('Omaha', 'Chicago', 4, ['blue']),
            ('Dallas', 'Little Rock', 2, ['grey']),
            ('Oklahoma City', 'Little Rock', 2, ['grey']),
            ('Houston', 'New Orleans', 2, ['grey']),
            ('New Orleans', 'Little Rock', 3, ['green']),
            ('Little Rock', 'Saint Louis', 2, ['grey']),
            ('Kansas City', 'Saint Louis', 2, ['blue', 'purple']),
            ('Little Rock', 'Nashville', 3, ['white']),
            ('Nashville', 'Saint Louis', 2, ['grey']),
            ('Saint Louis', 'Chicago', 2, ['green', 'white']),
            ('Sault St Marie', 'Toronto', 2, ['grey']),
            ('Sault St Marie', 'Montreal', 5, ['black']),
            ('Montreal', 'Toronto', 3, ['grey']),
            ('Montreal', 'Boston', 2, ['grey', 'grey']),
            ('Montreal', 'New York', 3, ['blue']),
            ('Toronto', 'Pittsburgh', 2, ['grey']),
            ('Toronto', 'Chicago', 4, ['white']),
            ('Boston', 'New York', 2, ['yellow', 'red']),
            ('New York', 'Pittsburgh', 2, ['green', 'white']),
            ('New York', 'Washington', 2, ['orange', 'black']),
            ('Pittsburgh', 'Chicago', 3, ['orange', 'black']),
            ('Pittsburgh', 'Saint Louis', 5, ['green']),
            ('Pittsburgh', 'Nashville', 4, ['yellow']),
            ('Pittsburgh', 'Raleigh', 2, ['grey']),
            ('Pittsburgh', 'Washington', 2, ['grey']),
            ('Washington', 'Raleigh', 2, ['grey', 'grey']),
            ('Raleigh', 'Nashville', 3, ['black']),
            ('Nashville', 'Atlanta', 1, ['grey']),
            ('Atlanta', 'Raleigh', 2, ['grey', 'grey']),
            ('Raleigh', 'Charleston', 2, ['grey']),
            ('Atlanta', 'New Orleans', 4, ['yellow', 'orange']),
            ('Atlanta', 'Charleston', 2, ['grey']),
            ('Miami', 'Charleston', 4, ['purple']),
            ('Miami', 'Atlanta', 5, ['blue']),
            ('Miami', 'New Orleans', 6, ['red'])
        ]