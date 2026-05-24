import requests
from bs4 import BeautifulSoup
import pandas as pd 
from pathlib import Path

csv_file = Path(__file__).parent.parent/ "data" / "trustpilot_reviews.csv"

def read_csv():
    return pd.read_csv(csv_file)
    



def scrape_reviews():
    pass

if __name__ == "__main__":
    print(read_csv())