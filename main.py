from bs4 import BeautifulSoup

url='testWebsite.html'


with open(url,'r') as html_file:
    #reading page as a file in html_files, and reading content of files in content variable
    content=html_file.read()

    #creating instance "soup"  of beautifulSoup in 'lxml' format to play with specific tag extraction
     
    soup= BeautifulSoup(content,'lxml')

    #finding all data with h1 tags
    tags= soup.find_all('h1')

    #extracting just the text info under tags
    for  tex in tags:
        print(tex.text)

