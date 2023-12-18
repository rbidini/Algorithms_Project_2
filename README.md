# Flight Route Optimization Web Application

## Overview
This web-based application, developed using Flask, optimizes flight route capacities between cities. The primary objective is to provide an efficient and accessible tool for finding the maximum flight capacity between selected destinations, complete with data visualization capabilities.

## Key Features
- **Flight Capacity Optimization:** Utilizes the Edmond-Karp algorithm to compute maximum capacity paths within a network of flights.
- **User-Friendly Interface:** Easy-to-use interface for inputting source and destination cities, enhancing user experience.
- **Detailed Flight Information:** Provides comprehensive information on flight routes, including maximum capacity paths, plane model, carrier, and distance.
- **Robust Error Handling:** Guides users through input errors such as non-existent cities or identical source and destination entries.

## Technologies Used
- Flask
- Python
- HTML/CSS
- JavaScript

## Installation and Usage
1. Clone the repository:
   ```
   git clone https://github.com/rbidini/Algorithms_Project_2
   ```
2. Navigate to the project directory and install dependencies.
3. Run the Flask application.
4. Access the application through the local host URL provided.

## Future Extensions
- Transition to a key-value database for efficient data management.
- Scale the web application to a public web server.
- Integrate more interactive dashboard features.
- Implement user preferences for personalized flight searches.
- Optimize the underlying algorithm for enhanced performance.
- Develop an API for fetching flight capacity data.

## Contributing
Contributions to this project are welcome. Please feel free to fork the repository, make changes, and submit pull requests. For major changes, open an issue first to discuss what you would like to change.

## Dependencies

Before running the script, ensure you have the required packages installed:
```bash
pip install -r requirements.txt
```
