## Analysis of Airline Routes from New York to San Francisco

### Graph Structure Ideas

**Nodes**:
- Each airport could be a node in the graph.
- We can represent the airport by its unique identifier (like the IATA code).

**Edges**: 
- Each flight between two airports could be an edge. We should probably use directed edges from source airport to destination airport.

**Weights**:
- Capacity (whenever we figure out how to calculate that).

### Algorithm Suggestions

- Depth-First Search (DFS) and Breadth-First Search (BFS) can be considered for initial exploration.
- It sounded like the professor wants us to use one of the Network Connectivity Algorithms for detailed analysis. We can explore some options or see what he will cover in class first.

### Plane Capacity Information
#### Note this is the **max** number of seats for each aircraft, _not accounting for crew members_
(If there are two or more variations for one aircraft {i.e. Airbus A320}, take the total number of seats for all of them, divide by
the number of different layouts. If decimal is average, take the floor value)

Using the following website: https://www.seatguru.com/airlines/Delta_Airlines/Delta_Airlines_Airbus_A321.php

- **Airbus A318**: 132 seats
- **Airbus A319**: 132 seats
- **Airbus A320**: 158 seats
- **Airbus A321**: 192 seats
- **Airbus A330**: 278 seats
- **Airbus A330-200**: 234 seats
- **Airbus A330-300**: 293 seats
- **Airbus A340**: 440 sets
- **Airbus A340-300**: 440 seats
- **Airbus A340-500**: 375 seats
- **Airbus A340-600**: 475 seats
- **Airbus A380-800**: 520 seats
- **Boeing 717**: 110 seats
- **Boeing 737**: 124 seats
- **Boeing 737-300**: 149 seats
- **Boeing 737-400**: 189 seats
- **Boeing 737-600**: 113 seats
- **Boeing 737-700**: 124 seats
- **Boeing 737-800**: 160 seats
- **Boeing 737-900**: 175 seats
- **Boeing 747**: 660 seats
- **Boeing 747-400**: 366 seats
- **Boeing 757**: 157 seats
- **Boeing 757-200**: 162 seats
- **Boeing 757-300**: 232 seats
- **Boeing 767**: 375 seats
- **Boeing 767-200**: 290 seats
- **Boeing 767-300**: 148 seats
- **Boeing 767-400**: 409 seats
- **Boeing 777**: 388 seats
- **Boeing 777-200**: 308 seats
- **Boeing 777-200LR**: 292 seats
- **Boeing 777-300**: 350 seats
- **Boeing 777-300ER**: 396 seats
- **Boeing 787**: 240 seats
- **Boeing 787-8**: 231 seats
- **Canadair Regional Jet 700**: 78 seats
- **Canadair Regional Jet 900**: 88 seats
- **De Havilland Canada DHC-8-300 Dash 8**: 50 seats
- **De Havilland Canada DHC-8-400 Dash 8Q**: 50 seats
- **Embraer 170**: 76 seats
- **Embraer 175**: 69 seats
- **Embraer 190**: 100 seats
- **Embraer EMB 120 Brasilia**: 30 seats
- **Embraer RJ140**: 44 seats
- **Embraer RJ145**: 50 seats
- **McDonnell Douglas MD-88**: 149 seats
- **McDonnell Douglas MD-90**: 158 seats

## Dependencies

Before running the script, ensure you have the required packages installed:
```bash
pip install -r requirements.txt
```
