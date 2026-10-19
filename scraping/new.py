import requests
from bs4 import BeautifulSoup

def scrape_us_gdp():
    url = "https://data.worldbank.org/country/united-states"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        gdp_element = soup.find("span", class_="value")
        if gdp_element:
            gdp = gdp_element.text.strip()
            print(f"United States GDP: {gdp}")
        else:
            print("Failed to find GDP data on the website.")
    else:
        print("Failed to retrieve data from the website.")

if __name__ == "__main__":
    scrape_us_gdp()
