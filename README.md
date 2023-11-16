## Analysis of Airline Routes from New York to San Francisco

### Graph Structure Ideas

**Nodes**:
- Each airport could be a node in the graph.
- We can represent the airport by its unique identifier (like the IATA code).

**Edges**: 
- Each flight between two airports could be an edge. We should probably use directed edges from source airport to destination airport.

**Weights**:
- Passenger load (whenever we figure out how to calculate that).

### Algorithm Suggestions

- Depth-First Search (DFS) and Breadth-First Search (BFS) can be considered for initial exploration.
- It sounded like the professor wants us to use one of the Network Connectivity Algorithms for detailed analysis. We can explore some options or see what he will cover in class first.

### Plane Models Information

**Wide-Body Aircraft**:
- *Airbus A330-200*: Typically seats 250-290 passengers in two-class or three-class configurations.
- *Airbus A330-300*: Up to 440 passengers, 300 in a two-class configuration.
- *Airbus A340-300*: Maximum 440 passengers, 295 in a three-class configuration.
- *Airbus A340-600*: Carries 475 passengers, 380 in a typical three-class configuration.
- *Airbus A380-800*: Largest passenger airplane, seats up to 853 in a single-class configuration, typically 525 in a three-class configuration.
- *Boeing 747-400*: Features a seating capacity of 524 in a two-class configuration and 416 in a three-class configuration.
- *Boeing 747-8 Intercontinental*: Accommodates a maximum of 467 passengers in a three-class configuration.
- *Boeing 777-200*: With a maximum seating capacity of 440, offers 305 seats in a three-class configuration and 400 in a two-class configuration.
- *Boeing 777-200LR*: A variant of the 777-200 with a longer range, typically seats the same number of passengers.
- *Boeing 777-300*: Offers a maximum capacity for 550 passengers, with 368 seats in a three-class configuration.
- *Boeing 777-300ER*: Extended Range variant of the 777-300, similar in passenger capacity.
- *Boeing 787-8*: Typically seats 242 passengers in a three-class configuration.
- *Ilyushin Il-96-400*: A Russian wide-body aircraft offering seating for 436 in a single-class configuration, 386 in a two-class, and 315 in a three-class configuration.

**Narrow-Body Aircraft**:
- *Airbus A318*, *A319*, *A320*, *A321*: Narrow-body variants with seating capacities ranging from 100 (A318) to 240 passengers (A321) depending on the configuration.
- *Boeing 717*: Typically seats around 115 passengers.
- *Boeing 737* (All Variants): Ranges from about 85 in the smallest variant to up to 215 passengers in the largest variant.
- *Boeing 757-200*, *757-300*: Seat between 200 (757-200) and 280 passengers (757-300).
- *Canadair Regional Jet 700*, *900*: Seating capacities of about 70 (CRJ700) and 90 passengers (CRJ900).
- *De Havilland Canada DHC-8-300 Dash 8*, *DHC-8-400 Dash 8Q*: Typical turboprop aircraft seating around 50-78 passengers.
- *Embraer 170*, *175*, *190*, *EMB 120 Brasilia*, *RJ140*, *RJ145*: Regional aircraft with capacities ranging from 30 (EMB 120) to 100 passengers (E190).
- *McDonnell Douglas MD-88*, *MD-90*: Seating typically ranges from 130 to 172 passengers.

## Dependencies

Before running the script, ensure you have the required packages installed:
```bash
pip install -r requirements.txt
```