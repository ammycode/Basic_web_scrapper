# demo to scrape a real world website

from bs4 import BeautifulSoup as bs
import requests
#request library to request info from a website

url="https://stackoverflow.com/jobs/companies?tl=data"

response_code= requests.get(url)

#extract html of website as text
html_text=requests.get(url).text
soup= bs(html_text,'lxml')

'''
<p class="mt8 mb0 fs-body1 fc-black-700 v-truncate2">Industry-leading. Difference-making. Tomorrow-shaping. These are just few of the adjectives used to describe the technologies and companies we work with every day. Join Deloitte, and those adjectives could also be describing your career.
Discover your impact
Make the most of disruptive technologies. Find the value in emerging business models. Turn technology from something...</p>'''

company_html1= soup.find('h2',class_='fs-body2 mb4')

company_descrption=soup.find('p',class_='mt8 mb0 fs-body1 fc-black-700 v-truncate2').text.split('\n')
company_name=company_html1.find('a').text
print(company_descrption[0])