import pickle
file = open("dictionary.txt", "wb")

my_dict  = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'hight': '[1,3,5,7]', 'weight': 'Female'}}


pickle.dump(my_dict, file)
file.close()



with open('dictionary.txt', 'rb') as f:
    data = f.read()
d = pickle.loads(data)


print(d)

new=[]
for k,v in my_dict.items():
    new.append(v.keys())

print(new)


#DEN MPOROUSA NA SINEXISO NA BRO TO KLIDI POY EMFANIZETE TIS PERISSOTERES FORES
