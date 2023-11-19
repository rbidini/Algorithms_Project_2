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

- **Airbus A220**: 109 seats
- **Airbus A318**
- **Airbus A319**: 132 seats
- **Airbus A320**: 158 seats
- **Airbus A321**: 192 seats
- **Airbus A321neo**: 196 seats
- **Airbus A330-200**: 234 seats
- **Airbus A330-300**: 293 seats
- **Airbus A330-900neo**: 281 seats
- **Airbus A340-300**
- **Airbus A340-600**
- **Airbus A350-900**: 306 seats
- **Airbus A380-800**
- **Boeing 717-200**: 110 seats
- **Boeing 737-300**
- **Boeing 737-400**
- **Boeing 737-600**
- **Boeing 737-700**: 124 seats
- **Boeing 737-800**: 160 seats
- **Boeing 737-900**: 175 seats
- **Boeing 737-900ER**: 180 seats
- **Boeing 737-Max 9**: 179 seats
- **Boeing 747**
- **Boeing 747-400**
- **Boeing 757-200**: 162 seats
- **Boeing 757-300**: 232 seats
- **Boeing 767**
- **Boeing 767-200**
- **Boeing 767-300**: 148 seats
- **Boeing 767-300ER**: 198 seats
- **Boeing 767-400**
- **Boeing 767-400ER**: 242 seats
- **Boeing 777**
- **Boeing 777-200**: 308 seats
- **Boeing 777-200ER**: 292 seats
- **Boeing 777-200LR**: 292 seats
- **Boeing 777-300**: 350 seats
- **Boeing 777-300ER**
- **Boeing 787**
- **Boeing 787-8**: 231 seats
- **Boeing 787-9**: 254 seats
- **Boeing (Douglas) MD-88**: 149 seats
- **Boeing (Douglas) MD-90**: 158 seats
- **Bombardier CRJ-200**: 50 seats
- **Bombardier CRJ-700**: 69 seats
- **Bombardier CRJ-900**: 70 seats
- **Canadair Regional Jet 700**
- **Canadair Regional Jet 900**
- **De Havilland Canada DHC-8-300 Dash 8**
- **De Havilland Canada DHC-8-400 Dash 8Q**
- **Embraer 170**: 70 seats
- **Embraer 175**: 76 seats
- **Embraer EMB 120 Brasilia**
- **Embraer ERJ-170**: 72 seats
- **Embraer ERJ-175**: 78 seats
- **Embraer ERJ-190**: 100 seats
- **Embraer RJ140**
- **Embraer RJ145**
- **McDonnell Douglas MD - 88**: 149 seats
- **McDonnell Douglas MD - 90-30**: 158 seats

## Dependencies

Before running the script, ensure you have the required packages installed:
```bash
pip install -r requirements.txt
```
