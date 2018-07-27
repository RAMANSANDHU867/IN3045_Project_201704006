Q:-1.division


x = 40
y = 4
z = x/y
print (z)






Q:- 2.swap two numbers




x = 100
y = 60


temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))






Q:-3

x = int(input("input 1st number: "))
y = int(input("input 2nd number: "))
z = int(input("input 3rd number: "))
n =x*y*z
print(n)






Q:-4

x = int(input("input a number: "))

for i in range(1,11):
    print(x,'n',i,'=',x*i)





Q:-5


x = int(input("input 1st number: "))
y = int(input("input 2nd number: "))
z = int(input("input 3rd number: "))
t = int(input("input 3rd number: "))

n =x+y+z+t
a= n/4
print(a)



Q:-6

x=int(input("enter your age "))

if x > 20:
    print("you are elder ")
elif x == 20:
    print("your are 20 years old")
else:
    print("your are younger")





Q:-7


 x = int(input("input 1st number: "))
y = int(input("input 2nd number: "))


if x == y:
    sum = x+y
    sum = sum*3
    print(sum)

else:
    z = x+y
    print(z)






Q:-8


while True:
   x = int(input("enter a number between 20 and 200: "))
   if 20 <= x <= 200:
      break
   print('try again')






Q:-9 BONUS


names_array=['jordan','debbie','john','jenelle','tony','suzan','tim','alicia','jordan','jeff']
print("length of names_array is " + str(len(names_array)))
searchForWho=input("who are you searching for ?")
for i in range(0,len(names_array)):
    thisName=names_array[i]
    if(thisName.find(searchForWho) > -1):
        print("found it..",searchForWho, "in position ",i)

else:
    print(" not found")
