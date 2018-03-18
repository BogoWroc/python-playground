import pandas as pd



airports = pd.read_csv('../resources/airports.csv')
airport_freq = pd.read_csv('../resources/airport-frequencies.csv')
runways = pd.read_csv('../resources/runways.csv')

print(airports.type.unique())


print(airports[:3])
print(airports['type'])
