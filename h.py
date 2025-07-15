*haed,tail=[1,2,3]
l = [ 1,3,24,5,5]
l[1::2]

l= [2,4,6,8,10,7,5]

[ a+4 for a in l ]
[ a for a in l if a%2==0]

[ v for p,v in enumerate(l) if p%2==0]
for v in zip(range(len(l)),l):
     print(v)

a = [1,2,4,5]
b = [1,5,2,6]
for f,s in zip(a,b):
    if f+s==7:
     print((f,s))

a =[ (x,y) for x,y in zip(a,b) if x+y==7 ]     
print(a)
l = [4,5,2,7,8]     
[ v-p for v,p in zip(l,range(len(l)))]
print([a+b for a,b in zip(l,l[1:])]) 

class Person:
   def __init__(self,name,year):
      self.name = name
      self.year = year

      
      



