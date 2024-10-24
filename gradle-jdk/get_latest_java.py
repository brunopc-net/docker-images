import requests
from bs4 import BeautifulSoup
import re

url = "https://hub.docker.com/layers/library/eclipse-temurin/21-jdk-alpine/images/sha256-76d1a7ee721d64f94678c9ef126258e3e3a6f988ff2b152f3ef8bfa7c499ff28?context=explore"

def get_latest_java_version():

    # Fetch the HTML content
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses

    content = response.text

    # Extract the Java version using regex
    match = re.search(r'JAVA_VERSION=jdk-(\d+\.\d+\.\d+)', content)

    # Output the Java version
    if match:
        java_version = match.group(1)
        print(f"Java version: {java_version}")
    else:
        print("Java version not found.")

if __name__ == "__main__":
    get_latest_java_version()