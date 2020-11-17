import requests
from bs4 import BeautifulSoup


file = open("data.txt","w+")
URL = 'https://www.bansiamo.it/bans_lista_completa_'
for i in range(1, 21):
    page = requests.get(URL + str(i) + '.html')
    soup = BeautifulSoup(page.content, 'html.parser')
    risultati = soup.find_all('div', class_='col-md-7 hidden-xs')
    for elem in risultati:
        link = elem.find('a')['href']
        file.write(link+"\n")