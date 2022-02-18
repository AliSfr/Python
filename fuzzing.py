import requests
with open("fuzzing.txt","r",encoding="utf-8") as file:
    icerik = file.read()
for i in icerik.split("\n"):
    url = "http://www.website.com"+str(i)
    response = requests.get(url=url)
    if response.status_code == 200:
        print(" + : ",str(i))
    else:
        print(" - : ",str(i))