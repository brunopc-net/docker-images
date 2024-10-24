import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re

url = "https://hub.docker.com/layers/library/eclipse-temurin/21-jdk-alpine/images/sha256-76d1a7ee721d64f94678c9ef126258e3e3a6f988ff2b152f3ef8bfa7c499ff28?context=explore"

def get_latest_java_version():

    # Fetch the HTML content
    session = HTMLSession()
    r = session.get(url)
    r.html.render(sleep=5, timeout=10)

    to_search = "JAVA_VERSION=jdk-"
    result = r.html.find(f'p:contains("{to_search}")', first=True).text
    java_version = result.split(to_search)[1]

    print(f"Java version: {java_version}")

if __name__ == "__main__":
    get_latest_java_version()