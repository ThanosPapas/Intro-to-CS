import requests
import json

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36'}
cnt=1 #global μεταβλητή που τη θέλω για να εκτυπώνω την εκάστοτε μέρα στη συνάρτηση

def getNum(diction):
    global cnt
    print(f"Στατιστικά {cnt}ης Δεκεμβρίου:")
    print(diction['content'][-1]["winningNumbers"]) #παίρνω το τελευταίο στοιχείο της λίστας επειδή έχει πάντα το μικρότερο drawId,άρα είναι και η πρώτη κλήρωση της ημέρας.
    cnt+=1

#καλώ σελίδα για την κάθε μέρα γιατί αν βάλω μεγαλύτερο range στο url
#η σελίδα του ΟΠΑΠ βγάζει σφάλμα, σας το είχα πει στο μάθημα και είπατε να το κάνουμε έτσι
print("Στατιστικά νικητήριων αριθμών πρώτης κλήρωσης για τον μήνα Δεκέμβρη")
print("="*100)
for i in range(1, 32):
    html = requests.get(f'https://api.opap.gr/draws/v3.0/1100/draw-date/2020-12-{str(i).zfill(2)}/2020-12-{str(i).zfill(2)}', headers=headers) #zfill γιατί τα url πάνε 01,02...
    html = html.text                                                                                                                           #Μετατροπή με str γτ η zfill δέχεται μόνο strings
    x = json.loads(html)
    getNum(x)