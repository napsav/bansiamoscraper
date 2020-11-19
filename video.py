import json
bans_file = open("bans.json", "r")
f = open("listamp4.txt", "w+")
fwebm = open("listawebm.txt", "w+")

bans = json.loads(bans_file.read())

def getVideos():
    for i, ban in enumerate(bans):
        if("video" in ban and (not ban["youtube"])):
            f.write(ban["video"] + "\n")
            fwebm.write(ban["video-audio"] + "\n")
        print(i)




faudio = open("audio.txt", "w+")

def getAudios():
    for i, ban in enumerate(bans):
        if("audio" in ban):
            faudio.write(ban["audio"] + "\n")
        print(i)

if __name__ == "__main__":
    getAudios()