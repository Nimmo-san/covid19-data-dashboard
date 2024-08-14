import requests
import pandas as pd
import psycopg2

# Fetch data from the COVID-19 API
url = 'https://api.covid19api.com/summary'
response = requests.get(url)
data = response.json()

# Convert data to a DataFrame
countries_data = data['Countries']
df = pd.DataFrame(countries_data)

# Insert data into PostgreSQL
conn = psycopg2.connect(
    dbname='covid19_data',
    user='yourusername',
    password='yourpassword',
    host='localhost'
)
cursor = conn.cursor()

# Iterating through the data and adding it to the covid_stats table
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO covid_stats (country, total_cases, total_deaths, total_recovered)
        VALUES (%s, %s, %s, %s)
    """, (row['Country'], row['TotalConfirmed'], row['TotalDeaths'], row['TotalRecovered']))

conn.commit()
cursor.close()
conn.close()

