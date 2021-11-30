gs = []
fb = []
bjk = []

def takim_ayir(satır):

    satır = satır[:-1]
    liste = satır.split(",")
    isim = liste[0]
    takim = liste[1]

    if (takim == "Galatasaray"):

        gs.append(isim)
    
    elif(takim == "Beşiktaş"):

        bjk.append(isim)
        
    else:
        fb.append(isim)
        
    
with open("futbolcular.txt","r") as file:
    for i in file:
        takim_ayir(i)

with open("gs.txt","w",encoding = "utf-8") as gs_takim:
    for i in gs:
        gs_takim.write(i)

with open("fb.txt","w",encoding = "utf-8") as fb_takim:
    for i in fb:
        fb_takim.write(i)

with open("bjk.txt","w",encoding = "utf-8") as bjk_takim:
    for i in bjk:
        bjk_takim.write(i)


        
        
        
