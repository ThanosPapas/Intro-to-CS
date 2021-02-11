import random
from math import ceil #για να κάνω τη στρογγυλοποίηση προς τα πάνω

def tetr(x):
    rows, cols = (x, x)
    arr = [[0 for i in range(rows)] for j in range(cols)] #αρχικοποίηση πίνακα με 0
    total = rows * cols
    mesos = 0
    for i in range(100):
        for i in range(ceil(total / 2)):
            while True: #loop για να μην μπει το 1 περισσότερες φορές σε μία θέση, που θα καταλήξει να μην γεμίσουν με 1 οι μισές θέσεις
                x = random.randint(0, rows -1)
                y = random.randint(0, cols-1)
                if arr[x][y] == 0:
                    arr[x][y] = 1
                    break
        for i in arr: #εκτύπωση πίνακα για επαλήθευση αποτελεσμάτων
            print(i)
        cnt = 0
        for i in range(rows): #έλεγχος για τετράδες, βάζω exceptions για να μην σκάσει το πρόγραμμα όταν βγει εκτός range η λίστα
            for j in range(cols):
                if arr[i][j] == 1:
                    try:
                        if arr[i][j] == arr[i][j+1] == arr[i][j+2] == arr[i][j+3]: #οριζόντια
                            cnt+=1
                    except IndexError:
                        pass
                    try:
                        if arr[i][j] == arr[i+1][j] == arr[i+2][j] == arr[i+3][j]: #κάθετα
                            cnt+=1
                    except IndexError:
                        pass
                    try:
                        if arr[i][j] == arr[i+1][j+1] == arr[i+2][j+2] == arr[i+3][j+3]: #διαγώνια προς δεξιά
                            cnt+=1
                    except IndexError:
                        pass
                    try:
                        if j > 2: #διαγώνια προς αριστερά, αυτή τη συνθήκη τη βάζω για να μη μου βγει απ' το τέλος το row, μου πήρε άπειρη ώρα για να βρω αυτό το bug!
                            if arr[i][j] == arr[i + 1][j - 1] == arr[i + 2][j - 2] == arr[i + 3][j - 3]:
                                cnt+=1
                    except IndexError:
                        pass
        print(cnt)
        mesos += cnt #αποθήκευση όλων των count για υπολογισμό του μέσου όρου
        arr = [[0 for i in range(rows)] for j in range(cols)] #επαναρχικοποίηση πίνακα για επανάληψη της διαδικασίας
    print(f"Ο μέσος όρος εμφάνισης τετράδων του 1 είναι: {mesos/100}")

while True:
    x = input("Βάλτε αριθμό: ") #loop ελέγχου μέχρι να εισαχθεί αριθμός
    try:
        tetr(int(x))
        break
    except ValueError:
        print("Αυτό δεν είναι αριθμός.", end=" ")
