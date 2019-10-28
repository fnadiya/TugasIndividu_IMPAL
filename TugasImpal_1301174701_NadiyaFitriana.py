a = int(input("Sisi 1 = "))
b = int(input("Sisi 2 = "))
c = int(input("Sisi 3 = "))

if(a<0 or a==0 ):
  print("segitiga tidak dapat dibangun")
elif(b<0 or b==0):
  print("segitiga tidak dapat dibangun")
elif(c<0 or c==0):
  print("segitiga tidak dapat dibangun")

if(a>0 and b>0 and c>0):
  x=max(a,b,c)
  if(a==b and b==c):
    print("segitiga sama sisi")
  elif (a==b or a==c or a==c):
    print ("segitiga sama kaki")
  elif(a**2 + b**2==c**2 or a**2 + c**2==b**2 or b**2 + c**2==a**2):
    print("segitiga siku-siku")
  else :
    print("segitiga bebas")

#tolong Pak jangan dibuka langsung di IDE mungkin tidak bisa di run
#alternatif source code => https://repl.it/@NadiyaFitriana1/SmallRuddyAssignments