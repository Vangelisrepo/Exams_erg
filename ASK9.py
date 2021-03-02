x=input("Δωστε το ονομα του αρχειου ASCII (πρεπει να εχει μορφη ονομα.txt) \n")
f=open( x , "r") #anoigi to arxio
k=f.read() # ekxori stin metabliti k olo to periexomeno toy arxeioy
s=str(k) #to kani tipy string vste na mporoyme na to baloyme se lista
s=list(s) #to balame se lista opoy kaue xaraxtiras einai diaforetikso px [x,r,t,]

u=0 #metabliti gia na metrame posa grammata exoume stin lista
moni=[] #ftiaxno mia lista gia na mpoyn oi monoi arithmi
for i in s: #mpeni mesa stin listas kai kani prospelasi ena ena xaraktira
    m=ord(i) #kathe metatropi ekxorite stin timi m
    if(m%2!=0): #gia na einai monos prepei mod 2 na einai 0 ara edo elexei oti o arithmos mod 2 den einai 0 ara einai monos
        moni.append(m) #bazoume toys arithmous stin lista monoi toys monous
        u=u+1 ##metabliti gia na metrame posa grammata exoume stin lista



forespouiparxikathegramma=[] #ftiaxnoume mia lista gia na doume poses fores iparxi kathe gramma
for i in moni: #prospelasi stin lista moni
    forespouiparxikathegramma.append(moni.count(i))  #pername stin lista poses fores iparxei kathe gramma




pososto=[] #ftiaxmoume lista gia na apothikefsoume  to pososto poy iparxei kathe ena gramma
for i in forespouiparxikathegramma: #prospelasi stin lista me ta grammata
    x1=forespouiparxikathegramma[i] #prajis gi pososto
    x1=x1/u #prajis gi pososto
    x1=x1*100 #prajis gi pososto
    pososto.append(x1) #to bazoume stin lista



stogilopososto=[] #ftiaxnoume lista gia na baloume strogilpoiimeno to pososto
import math
for i in pososto: #prospelasi stin lista possto gia strogilipoiisi
    stogilopososto.append(math.ceil(i)) #bazoume stin lista to stogilopoimeno pososto


new=[]
for i in moni:
    b=chr(i) #kanoume toys monous arithmous apo grammata se xaraktires
    new.append(b) #toys bazoume se mia adia lista
print("τα γραμμαρα οπου ο αντιστιχοσ αριθμοσ ASCI τουσ ειναι μονοσ ειναι" "\n")
print(new)
print("\n")
print("το ποσοστο τουσ ειναι αντιστοιχα")


for i in stogilopososto: #prospelasi stin lista strogilopososto
    print("\n")  # afini grammi kathe fora poy allazi arithmo mesa apo tin lista
    for j in range(i): # ektiponi asteraki
        print("*", end="") # ektiponi asteraki



f.close() 
