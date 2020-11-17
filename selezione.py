from bs4 import BeautifulSoup
import requests
import json
import urllib.parse

f = open("data.txt", "r", encoding="utf-8")
salvataggio = open("bans-audio-video.json", "w+", encoding="utf-8")
bans = f.readlines()
baseURL = 'https://www.bansiamo.it/'
bans_final = []
for i, x in enumerate(bans):
    no_vid = False
    no_aud = False
    page = requests.get(baseURL + x)
    soup = BeautifulSoup(page.content, "lxml", from_encoding='utf-8').prettify()
    soup = BeautifulSoup(soup, "lxml")
    print(str(i) + " - " + x)
    no_video = soup.find_all('img', src="img/video_no.png")
    no_audio = soup.find_all('img', src="img/audio_no.png")
    if len(no_video) > 0:
        no_vid = True
    if len(no_audio) > 0:
        no_aud = True
    divtesti = soup.find_all('div', class_="panel panel-testo")
    titolo = soup.find('div', class_="panel-heading text-center").text.strip()
    descrizione = divtesti[0].text.strip()
    testo = divtesti[1].find("div").text.strip()
    testo_clean = [line.strip() for line in testo.split('\n') if line.strip() != '']
    testostr = "\n".join(testo_clean)
    x =  {
        "titolo":titolo,
        "descrizione":descrizione,
        "testo":testostr,
    }
    if not no_vid:
        youtube_iframe = soup.find("iframe")
        if youtube_iframe is not None:
            youtube_video = youtube_iframe.get("src").replace('embed/', 'watch?v=')
            x['youtube']=True
            x['video']=youtube_video
        else:
            html5_video_audio = soup.find("video").find_all("source")
            
            video = baseURL + urllib.parse.quote(html5_video_audio[1].get("src"))
            audio = baseURL + urllib.parse.quote(html5_video_audio[0].get("src"))
            x['youtube']=False
            x['video']=video
            x['video-audio']=audio
    if not no_aud:
        audio = baseURL + urllib.parse.quote(soup.find("audio").find("source").get("src"))
        x['audio']=audio
    bans_final.append(x)
salvataggio.write(json.dumps(bans_final, indent=2))
print(str(i) + " completato\n")