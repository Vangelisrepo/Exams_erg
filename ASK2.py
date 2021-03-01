def Fibonacci(n):
    if n<=0:
        print("ΛΑΘΟΣ ΑΡΙΘΜΟΣ ")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)


x=input("Δωσε τον ορο τησ ακολουθιας  Fibonacci που θελεις να βρεις (πρεπει να ειναι αριθμος μεγαλυτερος η ισος του ενα )  \n ")
x=int(x)
k=Fibonacci(x)
if(x>0 and x!=1): #gia na gini o ipologismos prepei na elegxti pos den edose o xristis ton oro 0 i ton oro 1( o protos oros einai to 0)
	frasi1="o"
	frasi2="ορος τησ ακολουθιας Fibonacci ειναι"
	print(frasi1  + " " + str(x)+"ος" + " " + frasi2 + " " + str(k))
	print("Ας ελεχτει αν ειναι πρωτος ή οχι")



	import random
	numbers=[]
	for i in range(20) :
		y=random.randint(0,4000) #περναει στην μεταβλητη y μια τυχαια τιμη
		numbers.append(y)  #gemizi lista me tixaia τιμη ο πινακασ θα εχει 20 τυχαιεσ τιμεσ


	u=0
	for r in range(20): #προσπελαση τα νουμερα τησ λιστασ
		y=numbers[r]  #αποθηκευεει καθε νοθμερο σε μια μεταβλητη
		ipsosi=y**k  #κανει την πραξη  a^p=a mod p => a^p-a mod pγια να δοθμε  αν το αποτελεσμα ειναι 0 που θα ειναι πρωτος
		afer=ipsosi-y #κανει την πραξη  a^p=a mod p => a^p-a mod pγια να δοθμε  αν το αποτελεσμα ειναι 0 που θα ειναι πρωτος
		elegxos=afer%k  #κανει την πραξη  a^p=a mod p => a^p-a mod pγια να δοθμε  αν το αποτελεσμα ειναι 0 που θα ειναι πρωτος
		if(elegxos==0): #ελεγχει καθε μια απο τισ 20 τιμεσ αν ισχυει η παραπανω πραξη και αθξανει το u κατα 1
			u=u+1

	if(u==20): # αν το u  ειναι 20 σημαινει ολεσ οι τιμεσ στην λιστα τιρουν την πραξη αρα ειναι πρωτοσ
		print("ΕΙΝΑΙ ΠΡΩΤΟΣ ")
	else:
		print("ΔΕΝ ΕΙΝΑΙ ΠΡΩΤΟΣ ")
elif(k==0): #το βαζουμε σε περιπτωση που ο χρηστησ ζητησει τον πρωτο ορο ο οποιοσ ειναι 0 δεν μπορει να γινει διαιρεση με το 0 αρα παει σε αυτη την περιπτωση 
	print("Ο 1ος ΟΡΟΣ ΤΗΣ ΑΚΟΛΟΥΘΙΑΣ  ΕΙΝΑΙ ΤΟ 0 ΚΑΙ ΔΕΝ ΕΙΝΑΙ ΠΡΩΤΟΣ ")
else:
    print("Ο αριθμος πρεπει να ειναι μεγαλύτερος ή ισος του ενα προσπαθησε ξανα ")
