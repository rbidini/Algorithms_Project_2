import pandas as pd


# reading the CSV files
# some column names had empty spaces in the beginning of the name, "skipinitialspace=True" parameter removes empty spaces.
routes_data = pd.read_csv('data/routes.csv', encoding='ISO-8859-1', skipinitialspace=True)

airlines_data = pd.read_csv('data/airlines.csv', encoding='ISO-8859-1', skipinitialspace=True)

# assigning column names for airports file because names are not provided in the original file
col_names_airports = [
    'Airport ID',
    'Name',
    'City',
    'Country',
    'IATA',
    'ICAO',
    'Latitude',
    'Longitude',
    'Altitude',
    'Timezone',
    'DST',
    'Tz',
    'Type',
    'Source'
]
airports_data = pd.read_csv('data/airports-extended.csv', encoding='ISO-8859-1', names=col_names_airports)

# assigning column names for planes file because names are not provided in the original file
col_names_planes = [
    "Plane",
    "IATA",
    "ICAO"
]
planes_data = pd.read_csv('data/planes.dat.txt', encoding='ISO-8859-1', names=col_names_planes)


# handling missing values
# replacing '\N' with NaN for consistency
airports_data.replace('\\N', pd.NA, inplace=True)
airlines_data.replace('\\N', pd.NA, inplace=True)
routes_data.replace('\\N', pd.NA, inplace=True)
planes_data.replace('\\N', pd.NA, inplace=True)


# displaying the contents of the CSV files
def print_routes_data():
    """
    COLUMN NAMES:
    "airline": 2-letter or 3-letter code of the airline.
    "airline ID": Unique OpenFlights identifier for airline.
    "source airport": 3-letter or 4-letter code of the source airport.
    "source airport id": Unique OpenFlights identifier for source airport.
    "destination airport": 3-letter or 4-letter code of the destination airport.
    "destination airport id": Unique OpenFlights identifier for destination airport.
    "codeshare": "Y" if this flight is a codeshare (that is, not operated by Airline, but another carrier), empty
    otherwise.
    "stops": Number of stops on this flight ("0" for direct).
    "equipment": 3-letter codes for plane type(s) generally used on this flight, separated by spaces.
    """
    print(routes_data.to_string())


def print_airlines_data():
    """
    COLUMN NAMES:
    "Airline ID": ID Unique OpenFlights identifier for this airline.
    "Name:" Name of the airline.
    "Alias": Alias of the airline. For example, All Nippon Airways is commonly known as "ANA".
    "IATA": 2-letter IATA code, if available.
    "ICAO": 3-letter ICAO code, if available.
    "Callsign": Airline callsign.
    "Country": Country or territory where airline is incorporated.
    "Active": "Y" if the airline is or has until recently been operational, "N" if it is defunct.
    """
    print(airlines_data.to_string())


def print_airports_data():
    """
    COLUMN NAMES:
    "Airport ID": Unique OpenFlights identifier for this airport.
    "Name": Name of airport. May or may not contain the City name.
    "City": Main city served by airport. May be spelled differently from Name.
    "Country": Country or territory where airport is located. See countries.dat to cross-reference to ISO 3166-1 codes.
    "IATA": 3-letter IATA code. Null if not assigned/unknown.
    "ICAO": 4-letter ICAO code. Null if not assigned.
    "Latitude": Decimal degrees, usually to six significant digits. Negative is South, positive is North.
    "Longitude": Decimal degrees, usually to six significant digits. Negative is West, positive is East.
    "Altitude": In feet.
    "Timezone": Hours offset from UTC. Fractional hours are expressed as decimals, eg. India is 5.5.
    "DST": Daylight savings time. One of E (Europe), A (US/Canada), S (South America), O (Australia), Z (New Zealand),
    N (None) or U (Unknown). See also: Help: Time
    "Tz": database time zone Timezone in "tz" (Olson) format, eg. "America/Los_Angeles".
    "Type": Type of the airport. Value "airport" for air terminals, "station" for train stations, "port" for ferry
    terminals and "unknown" if not known.
    "Source": Source of this data. "OurAirports" for data sourced from OurAirports, "Legacy" for old data not matched to
    OurAirports (mostly DAFIF), "User" for unverified user contributions. In airports.csv, only source=OurAirports
    is included.
    """
    print(airports_data.to_string())


def print_planes_data():
    """
    COLUMN NAMES:
    "Plane": plane model
    "IATA",
    "ICAO"
    """
    print(planes_data.to_string())
