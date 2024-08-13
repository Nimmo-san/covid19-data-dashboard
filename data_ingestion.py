import requests 
import pandas as pd
import psycopg2

# Fetching the data from the api
url = 'https://api.covid19api.com/summary'
reponse = requests.get(url)
data = response.json()


# Converting the data into a DataFrame
countries_data = data['Countries']
df = pd.DataFrame(countries_data)

# pushing the data into postgresql
conn = psycopg2.connect(
	dbname='covid19_data',
	user='nemo',
	password='nemo',
	host='localhost')

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO covid_stats (country, total_cases, total_deaths, total_recovered)
        VALUES (%s, %s, %s, %s)
    """, (row['Country'], row['TotalConfirmed'], row['TotalDeaths'], row['TotalRecovered']))

conn.commit()
cursor.close()
conn.close() 
	
