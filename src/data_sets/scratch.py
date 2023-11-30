import pandas as pd

flights_data = pd.read_csv('final_all_flights.csv', encoding='ISO-8859-1', skipinitialspace=True)

if "new yrk" not in list(flights_data["source city"]):
    print("true")
