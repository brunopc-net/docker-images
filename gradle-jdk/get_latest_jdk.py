import requests
from bs4 import BeautifulSoup
import re

url = "https://gradle.org/release-checksums"

def get_latest_gradle_version_and_checksum():

    # Fetch the HTML content
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses

    # Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the latest version (assuming it's in a specific format)
    main = soup.find('main')
    latest_version = main.find('h3').get_text().split('v')[1]
    checksum = main.find('code').get_text()

    print(f"Latest_version: {latest_version}")
    print(f"Checksum: {checksum}")

if __name__ == "__main__":
    get_latest_gradle_version_and_checksum()