from bs4 import BeautifulSoup
import requests

f = open("data.txt", "r", encoding="utf-8")
salvataggio = open("bans-audio-video.txt", "w+", encoding="utf-8")
bans = f.readlines()
baseURL = 'https://www.bansiamo.it/'
bans_final = []
for i, x in enumerate(bans):
    no_vid = False
    no_aud = False
    page = requests.get(baseURL + x)
    print(page.encoding)
    soup = BeautifulSoup(page.content, "html.parser", from_encoding='utf-8').prettify()
    salvataggio.write(soup)
    soup = BeautifulSoup(soup)
    print(str(i) + " - " + x)
    no_video = soup.find_all('img', src="img/video_no.png")
    no_audio = soup.find_all('img', src="img/audio_no.png")
    if len(no_video) > 0:
        no_vid = True
    if len(no_audio) > 0:
        no_aud = True
    divtesti = soup.find_all('div', class_="panel panel-testo")
    descrizione = divtesti[0].text.strip()
    testo = divtesti[1].find("div").text
    testo_clean = [line.strip() for line in testo.split('\n') if line.strip() != '']
    testostr = "\n".join(testo_clean)
    
    print(descrizione)
    print(testo)
    if not no_vid:
        youtube_iframe = soup.find("iframe")
        if youtube_iframe is not None:
            youtube_video = youtube_iframe.get("src").replace('embed/', 'watch?v=')
            youtube = True
            print(youtube_video)
        else:
            youtube = False
            html5_video_audio = soup.find("video").find_all("source")
            video = html5_video_audio[1].get("src")
            audio = html5_video_audio[0].get("src")
            print(video)
            print(audio)
    print(str(i) + " completato\n")