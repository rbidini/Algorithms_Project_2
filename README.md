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
- *Airbus A380-800*: Largest passenger airplane, seats up to 853 (single-class), typically 525 (three-class).
- *Boeing 777-300*: Maximum 550 passengers, 368 (three-class).
- *Boeing 747-400*: Seats 524 (two-class), 416 (three-class).
- *Airbus A340-600*: Carries 475 passengers, 380 (three-class).
- *Boeing 747-8 Intercontinental*: Up to 467 passengers (three-class).
- *Boeing 777-200*: Maximum 440 passengers, 305 (three-class), 400 (two-class).
- *Airbus A330-300*: Up to 440 passengers, 300 (two-class).
- *Airbus A340-300*: Maximum 440 passengers, 295 (three-class).
- *Ilyushin Il-96-400*: Russian wide-body, seats 436 (single-class), 386 (two-class), 315 (three-class).
- *Airbus A340-500*: Maximum 375 passengers, 313 (three-class).

**Narrow-Body Aircraft** (Not included in sources):
- *Boeing 737*: Ranges from 85 to 215 passengers, depending on the variant.
- *Airbus A320*: Seats 140 to 240 passengers, model and configuration dependent.

## Dependencies

Before running the script, ensure you have the required packages installed:
```bash
pip install -r requirements.txt
```