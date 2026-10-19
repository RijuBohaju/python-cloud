import requests
from bs4 import BeautifulSoup
# Create a request to the World Bank's GDP data page
response = requests.get('https://data.worldbank.org/indicator/NY.GDP.MKTP.CD')
# Parse the HTML document
soup = BeautifulSoup(response.content, 'html.parser')
# Find the table of GDP data
table = soup.find('table', {'class': 'table table-striped table-bordered table-hover table-condensed'})
# Extract the data from the table
rows = table.find_all('tr')
# Create a list to store the data
data = []
# Iterate over the rows of data
for row in rows:
    # Extract the country name
    country = row.find('th').text
    # Extract the GDP data
    gdp = row.find('td').text
    # Add the data to the list
    data.append({'country': country, 'gdp': gdp})
# Print the data
print(data)