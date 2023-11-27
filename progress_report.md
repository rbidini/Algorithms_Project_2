# Algorithms Final Project - Group Blue (Hanna, Randy, Ray, Rosemary, Tim)

## 1. Data Organization
### Completed Data Analysis:
- Analyzed the structure, fields, and available data of routes, airlines, airports, and plane models datasets.
- Read data from CSV files using pandas, ensuring correct encoding and handling of initial space in column names.

### Completed Data Cleaning:
- Performed data cleaning by identifying and removing inactive airlines.
- Handled missing or inconsistent values, particularly in columns related to airports and routes.
- Assigned custom column names for datasets missing header rows.

### Completed Data Decoding:
- Established relationships between datasets by merging routes, airlines, airports, and plane models based on common identifiers.
- Decoded equipment codes by mapping them to corresponding plane models.
- Identified and combined flights of interest based on specific source and destination criteria (New York to San Francisco), including both direct and up to one layover flights.
- Filtered the data frame to retain only relevant columns to enhance data relevance and readability.
- Merged the flights data frame with plane capacities for each plane model.

### Completed Output Preparation:
- Saved the final dataset to a CSV file for future analysis.

## 2. Research
### In Progress Capacity Research:
- Gathering accurate capacity data for each plane model. Saved in `capacity.json` file.

### Completed Algorithm Research:
- We will implement a modified version of Dijkstra’s algorithm.

## 3. Implementation
### In Progress Algorithm Implementation
#### Graph Structure Ideas:
- **Nodes**: Each airport will be a node in the graph, represented by its unique identifier (like the IATA code).
- **Edges**: Create directed edges for flights from source to destination airports.
- **Weights**: Plane capacities.

## 4. Testing
### Not Ready
- Ensure that the algorithm works as expected.
- Analysis of performance, including time complexity.

## 5. Dashboard Implementation
### In Progress
- Development of a user-friendly interface for data interaction and visualization.

## 6. Final Report and Presentation
### In Progress
- Documentation of project process, findings, and conclusions.
### Not Ready
- Preparation of a presentation summarizing the key aspects of the project.

---

## Role Assignment
### Completed Data Organization: Hanna
- Data Analysis: Hanna
- Data Cleaning: Hanna
- Data Decoding: Hanna
- Output Preparation: Hanna
  - **Deadline**: 11-15-2023  11:59 PM

### In Progress Research: Tim, Randy, Ray, Hanna
- Algorithm Research: Tim, Randy, Ray, Hanna
- Capacity Research: Randy, Ray
  - **Deadline**: 11-19-2023  11:59 PM

### Not Ready Implementation: Ray and Tim (everyone else to assist)
- First Draft Deadline: 11-26-2023  11:59 PM
- Final Deadline: 12-03-2023  11:59 PM

### Not Ready Testing: Tim, Rosemary
- **Deadline**: TBD upon main algorithm completion

### In Progress Dashboard Implementation: Randy
- **Deadline**: 12-10-2023 (weekend before final presentation)

### Not Ready Final Report and Presentation: Rosemary
- **Deadline**: 12-10-2023 (weekend before final presentation)