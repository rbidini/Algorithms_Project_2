import pandas as pd


flights_data = pd.read_csv('data/final_max_capacity_flights.csv', encoding='ISO-8859-1')

print(flights_data.to_string())
