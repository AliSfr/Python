from bs4 import BeautifulSoup
import requests

# class Google:
#     def __init__(self,text):
#         self.text = text
#         result = requests.get("https://www.google.com/search?q="+self.text).content
#         self.soup = BeautifulSoup(result,"html.parser")
#
#     def search(self):
#         searches = self.soup.find_all("h3","LC20lb")
#         for i in searches:
#             print(i)
#
# text = input("Arama Çubuğu: ")
# google = Google(text)
# google.search()

def content(text):
    result = requests.get("https://www.google.com/search?q=" + text).content
    soup = BeautifulSoup(result, "html.parser")
    return soup

def search(text):
    soup = content(text)
    searches = soup.find_all("div","BNeawe vvjwJb AP7Wnd")
    for i in searches:
        print(i.text)

text = input("Arama Çubuğu: ")
search(text)



