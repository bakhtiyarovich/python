# for i in range(1,100):
#   if i % 2 == 0 :
#     print(i,"-juft")
#   else:
#     print(i,"-toq") 

a = int(input("son kiriting: "))
n  = 0
for i in range(2, a // 2+1):
    if (a % i == 0):
        n = n+1
if (n <= 0):
    print("tub son")
else: 
  print("tub emas")
