import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}

cnt = 1 #global μεταβλητή που τη θέλω για να εκτυπώνω την εκάστοτε μέρα στη συνάρτηση

def getNum(diction):
    global cnt
    leksiko = {} #δημιουργία λεξικού για σύγκριση τιμών
    lst = [] #δημιουργία λίστας που θα περιλαμβάνει τον αριθμό ή τους αριθμούς που εμφανίζονται πιο πολλές φορές κάθε μέρα
    for i in diction['content']:
        for j in i["winningNumbers"]['list']:
            if j not in leksiko.keys():
                leksiko[j] = 1
            else:
                leksiko[j] +=1
    max=0
    for j in leksiko.values(): #εύρεση μέγιστης τιμής
        if j > max:
            max = j
    for m in leksiko.keys(): #εύρεση κλειδιών με μέγιστη τιμή
        if leksiko[m] == max:
              lst.append(m)

    if len(lst) == 1:
        print(f"O αριθμός που εμφανίζεται περισσότερες φορές την {cnt}η Δεκεμβρίου είναι ο {lst[0]}")
    else:
        s = [str(i) for i in lst] #κάνω τα στοιχεία str για να μπορώ μετά να τα κάνω .join
        print(f"Οι αριθμοί που εμφανίζονται περισσότερες φορές την {cnt}η Δεκεμβρίου είναι οι: " + " , ".join(s))
    cnt+=1


for i in range(1, 22):
    if i < 10:
        html = requests.get(f'https://api.opap.gr/draws/v3.0/1100/draw-date/2020-12-0{i}/2020-12-0{i}', headers=headers)
    else:
        html = requests.get(f'https://api.opap.gr/draws/v3.0/1100/draw-date/2020-12-{i}/2020-12-{i}', headers=headers)
    html = html.text
    x = json.loads(html)
    getNum(x)

