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
    versions = soup.find_all(string=re.compile(r'v\d+\.\d+\.\d+'))
    latest_version = versions[0].split()[1] if versions else None
 
    # Find the checksum for the latest version
    checksum = None
    if latest_version:
        checksum_row = soup.find(string=latest_version).find_parent('tr')
        if checksum_row:
            checksum = checksum_row.find_all('td')[1].text.strip()

    # Output the results
    print(f"Latest Gradle Version: {latest_version}")
    print(f"Checksum: {checksum}")

if __name__ == "__main__":
    get_latest_gradle_version_and_checksum()