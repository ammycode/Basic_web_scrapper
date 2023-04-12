# demo to scrape a real world website

from bs4 import BeautifulSoup as bs
import requests
#request library to request info from a website

url="https://stackoverflow.com/jobs/companies?tl=data"

response_code= requests.get(url)

#extract html of website as text
html_text=requests.get(url).text
soup= bs(html_text,'lxml')

company_html= soup.find('h2',class_='fs-body2 mb4')
company_name=company_html.find('a').text
print(company_name)