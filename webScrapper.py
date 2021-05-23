import requests as req
from bs4 import BeautifulSoup
from csv import writer

response = req.get("https://webscraper.io/test-sites/e-commerce/allinone")
soup = BeautifulSoup(response.text, "html.parser")

with open("ecom_data.csv", "w") as csv_file:
    csv_writer= writer(csv_file)
    csv_writer.writerow(['title','link','description', 'price'])

    headings = soup.find_all('h4')
    para = soup.find(class_="description").get_text()
    for heading in headings:
        # title = heading.find("a").get_text()
        price = heading.find(class_="pull-right price")
        a_tag = heading.find("a")
        if a_tag is not None:
            title = a_tag.get_text()
            refrence = a_tag['href']
            csv_writer.writerow([title,refrence,para,price])