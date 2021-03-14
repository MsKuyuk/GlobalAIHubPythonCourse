çiftler_listesi = [0, 2, 4]
tekler_listesi = [1, 3, 5]
ortak_liste = tek_liste + çift_liste
birleştirilmiş_liste = ortak_liste.sort()
son_liste = list(ortak_liste)
son_liste = list([ i*2 for i in ortak_liste])
for i in son_liste:
    print(type(i))
    print(i)