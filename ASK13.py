x=input("Δωστε το ονομα του αρχειου ASCII (πρεπει να εχει μορφη ονομα.txt) \n")
f=open(x, "r") #anoigei to arxio pou edose o xrisths
k=f.read() #bazei to periexomeno toy stin metabliti k
k=k.split() #xorizei to keimeno ana leksis kai to bazi se mia lista px [a,letter,okei]
lst=[]
u=0 #bazouyme mia metabliti gia na metrame poses lejis exei mesa i lista
for i in k: #prospelasi stin list ame tis lejis
    lst.append(i) #bazoume stin lista lst kathe mia leji
    u=u+1 # metrame



mia=0
dio=[]   #ftiaxnoume mia lista gia na baloume enomena zeugaria lejeon
for i in range(0,len(lst)-1,1):
    dio.append(lst[i]+lst[i+1])    #bazoume stin lista ta zeugaria lejeon
    mia=mia+1 #metabliti poy metraei posa zeugaria lejeon exoume mesa stin lista dio


tpt=0 #metabliti gia na metraei posa zeugaria apo tin lista exoyn akribos 20 xaraktires
ok=[] #lista gia na bazoume ta zeugaria poy exoyn 20 xaraktires
for i in dio:
    if(len(i)==20): #elegxoume an exoyn
        ok.append(i) # an exoun ta bazoume mesa stin lista
    else:
        tpt=tpt+1 # mia metabliti poy aujanete otan den exoun kathe zeugari 20 xaraktires gia na doume an to athrisma tis bgei iso me osa kai ta zeugaria stin lista simenei pos den exeikanena zeugari 20 xaraktires


if(tpt==mia): # elegxei an ta zeugaria poy den exouneiani isa me ton arithmo ton zeygarion pou einai stin lista an nai tote kanena den exei 20 xaraktires akribos
    print("ΔΕΝ ΥΠΑΡΧΕΙ ΖΕΥΓΑΡΙ ΛΕΞΕΩΝ ΜΕ ΑΚΡΙΒΩΣ 20 ΧΑΡΑΚΤΗΡΕΣ")
else:
    print("20 ΧΑΡΑΚΤΗΡΕΣ ΕΧΟΥΝ ΤΑ ΠΑΡΑΚΑΤΩ ΖΕΥΓΑΡΙΑ ")
    print(ok)



f.close()
