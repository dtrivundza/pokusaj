"brojevi=[9,3,1,6,2,4,8,7]"
"brojevi.sort()"
"brojevi.reverse()"
"print(brojevi)"
'''
brojevi=[9,3,1,6,2,4,8,7]
while True:
    izvrsena_zamjena=False
    for i in range(1,len(brojevi)):
        if brojevi[i] < brojevi[i-1]:
            temp= brojevi[i]
            brojevi[i]= brojevi[i-1]
            brojevi[i-1]= temp
            izvrsena_zamjena=True
    if izvrsena_zamjena== False:
        break
print(brojevi)
'''
''''
proizvodi=["Telefon","TV","laptop"]
cijene=[100,200,300]
for x in range(len(proizvodi)):
    print(proizvodi[x],cijene[x])
'''
''''
automobili=["audi","BMW","Yugo","Citroen","Kia","Peugeot"]
for i in range(len(automobili)):
    if i==5:
        print("Aleksandra vozi auto:",automobili[i])
'''
''''
automobili=["audi","BMW","Yugo","Citroen","Kia","Peugeot"]
for i in range(len(automobili)):
    automobili[i]=automobili[i]+"2"
print(automobili)
'''


#telefoni=["iphone11","samsung32","xiaomi"]
#laptopovi=["acer","mcbook","del"]
#tableti=["ipad","samsung galaxy","xiaomi tablet"]

proizvodi=[ ["iphone11","samsung32","xiaomi"],
            ["acer","mcbook","del"],
            ["ipad","samsung galaxy","xiaomi tablet"]]
#print(proizvodi[1][2])
#proizvodi=[telefoni,laptopovi,tableti]
#for kategorija in proizvodi:
    #print(kategorija[0],kategorija[1],kategorija[2])
   # for stavka in kategorija:
   #     print(stavka)
#for i in range(len(proizvodi)):
  #  for j in range(len(proizvodi[i])):
   #     print(proizvodi[2][2])#

hrana= [
            ["cokolada","bombone","palacinke"],
            ["sarma","musaka","kiseli kupus"],
            ["pecena paprika","ajvar","sopska"]
]
for kategorija in hrana:
    for jelo in kategorija:
        print(jelo)

#ime="Sofija"
#poruka=f"Cao,{ime}"
#print(poruka)
#a=5
#b=7
#sabiranje=f"rezultat sabiranja {a} i {b} je {a+b}"
#print(sabiranje)
biblioteka=[]
while True:
    print("Odaberi komandu: 1-unos, 2-prikaz, 3-brisanje, > 3 izlaz")
    komanda = int(input("Unesite komandu: "))

    if komanda == 1:
        # unos knjige, preuzmi podatke
        naslov = input("Unesite naslov: ")
        autor = input("Unesite autora: ")
        isbn = int(input("Unesite isbn: "))
        biblioteka.append([naslov, autor, isbn])
        print("Dodata knjiga")
    if komanda == 2:
        for knjiga in biblioteka:
            for detalj in knjiga:
                print(detalj)
    if komanda == 3:
        #ovde vrsim brisanje
        kljucna_rec = input("Unesite naziv knjige koju zelite da obrisem. ")
        for knjiga in biblioteka:
            #proveravam detalje KNJIGE
            for detalj in knjiga:
                if detalj == kljucna_rec:
                    biblioteka.remove(knjiga)
                    print("Knjiga je obrisana")
        if knjiga >3:
            break
