ism = input("Enter name: ")
count = 1
dict1 = dict()
for i in ism:
  if i in dict1:
    dict1[i] +=1
  else:
    dict1[i] = 1

print(dict1)




