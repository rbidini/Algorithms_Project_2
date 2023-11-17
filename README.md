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

- **Airbus A220**: 105 seats
- **Airbus A319**: 128 seats
- **Airbus A320**: 150 seats
- **Airbus A321**: 185 seats
- **Airbus A321neo**: 196 seats
- **Airbus A330-200**: 230 seats
- **Airbus A330-300**: 290 seats
- **Airbus A330-900neo**: 280 seats
- **Airbus A350-900**: 300 seats
- **Boeing 717-200**: 110 seats
- **Boeing 737-700**: 126 seats
- **Boeing 737-800**: 165 seats
- **Boeing 737-900**: 180 seats
- **Boeing 737-900ER**: 180 seats
- **Boeing 737-Max 9**: 180 seats
- **Boeing 757-200**: 180 seats
- **Boeing 757-300**: 230 seats
- **Boeing 767-300**: 200 seats
- **Boeing 767-300ER**: 225 seats
- **Boeing 767-400ER**: 240 seats
- **Boeing 777-200**: 270 seats
- **Boeing 777-200ER**: 270 seats
- **Boeing 777-200LR**: 280 seats
- **Boeing 777-300**: 300 seats
- **Boeing 787-8**: 235 seats
- **Boeing 787-9**: 280 seats
- **Embraer ERJ-170**: 72 seats
- **Embraer ERJ-175**: 78 seats
- **Embraer 175**: 76 seats
- **Embraer 170**: 69 seats
- **Boeing (Douglas) MD-88**: 149 seats
- **Bombardier CRJ-200**: 50 seats
- **Boeing (Douglas) MD-90**: 158 seats
- **Embraer ERJ-190**: 100 seats
- **McDonnell Douglas MD - 88**: 150 seats
- **McDonnell Douglas MD - 90-30**: 150 seats
- **Bombardier CRJ-700**: 75 seats
- **Bombardier CRJ-900**: 75 seats

## Dependencies

Before running the script, ensure you have the required packages installed:
```bash
pip install -r requirements.txt
```