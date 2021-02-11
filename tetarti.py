import random

with open('ergasia.txt', 'r') as f:
    lst=[]
    remove = ',.()\'[]-!0123456789":;?'
    x = f.read()
    for i in remove: #αφαιρώ αγκύλες, παύλες κτλ απ' το κείμενο
        x = x.replace(i, '')
    text = x.lower().split()
    lst = []
    for i in range(len(text) + 1): #δημιουργία λίστας που περιέχει όλες τις πιθανές συνεχόμενες τριάδες λέξεων
        try:
            y = text[i] + " " + text[i+1]  + " " + text[i+2]
            lst.append(y)
        except IndexError:
            pass
    tyxaia = random.choice(lst).split() #επιλογή τυχαίας τριάδας και μετατροπή της σε λίστα για να μπορώ να την επεξεργαστώ
    print(tyxaia[1] + " " + tyxaia[2], end=' ') #ξεκίνημα κειμένου με τις δύο τελευταίες λέξεις της πρώτης τριάδας
    lst3 = [tyxaia[1], tyxaia[2]] #δημιουργία λίστας για έλεγχο, όταν φτάσει τις 200 λέξεις θα σταματήσει η επανάληψη
    while len(lst3) < 200:
        lst2=[] #δημιουργία λίστας που περιέχει όλα τα πιθανά matches, επαναρχικοποιείται μετά το τέλος του κάθε for
        for i in lst:
            i = i.split()
            if tyxaia[1]==i[0] and tyxaia[2]==i[1]:
                lst2.append(i)
        if not lst2: #αν η λίστα δεν είχε κανένα match διακόπτεται το πρόγραμμα
            break
        tyxaia = random.choice(lst2) #τυχαία επιλογή απ' όλα τα matches
        print(tyxaia[2], end=' ') #εκτύπωση τυχαίου κειμένου
        lst3.append(tyxaia[2])
