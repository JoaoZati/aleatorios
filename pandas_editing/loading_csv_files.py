import os
import pandas as pd

# os.getcwd()
# os.listdir()
# os.chdir(path)

csv_file = pd.read_csv('supermarkets.csv')
json_file = pd.read_json('supermarkets.json')
excel_file = pd.read_excel('supermarkets.xlsx', sheet_name=0)
csv_file_commas = pd.read_csv('supermarkets-commas.txt')
csv_file_semi_commas = pd.read_csv('supermarkets-semi-colons.txt')
csv_file_semi_commas_2 = pd.read_csv('supermarkets-semi-colons.txt', sep=";")

df_header = pd.read_csv('supermarkets.csv', header=None)
df_header.columns = csv_file.columns
df_header.index = df_header['Address']

#  Manipulate

df_manipulate = df_header
df_loc = df_manipulate.loc['3666 21st St':'332 Hill St', 'City': 'Country']
df_iloc = df_manipulate.iloc[1:3, 2::2]

#  Delete rows and lines

df_drop_city = df_header.copy()
df_drop_city.drop('City', 1, inplace=True)
df_drop_city.shape
df_drop_city.index.shape
df_T = df_drop_city.T

df_T['My Address'] = ['Cascavel', 'Parana', 'João', 'Paraná', 'America do Sul', 7]

from geopy.geocoders import ArcGIS

nom = ArcGIS()

cordenates = nom.geocode('735 Dolores St, San Francisco, CA 94119')
cordenates.latitude
cordenates.longitude

df = df_manipulate
df['Full Address'] = df['Address'] + ', ' + df['City'] + ', ' + df['State'] + df['Country']

address = df.iloc[1,:].loc['Full Address']
nom.geocode(address)

df['Geocode'] = df['Full Address'].apply(nom.geocode)
df.Geocode[1]
df.Geocode[1].latitude

df['Latitude'] = df['Geocode'].apply(lambda x: x.latitude if x != None else None)
df['Longitude'] = df['Geocode'].apply(lambda x: x.longitude if x != None else None)

