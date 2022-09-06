import requests
from bs4 import BeautifulSoup

req = requests.get("https://realpython.github.io/fake-jobs/")
soup = BeautifulSoup(req.content, "html.parser")
results = soup.find(id="ResultsContainer")
job_elements = results.find_all("div", class_="card-content")
for job_element in job_elements:
    title_element = job_element.find("h2" , class_="title")
    location_element = job_element.find("p", class_="location")
    print(title_element.text.strip())
    print(location_element.text.strip())
    print()