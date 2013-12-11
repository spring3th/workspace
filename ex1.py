#First Programe
print("Hello World!")
print("I like typing this.")

print("--------------------")
print("I will now count my chickens:")

print("Hens",25+30/6)

my_name = 'Zed A. Shaw'
my_age = 35 #not a lie
my_height = 74 #inches
my_weight = 180 #1bs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s." % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")

x = y = [1,2,3]
z = [1,2,3]
print(x == y)

print(x is y)
print(x is z)

print(y.reverse())

print("Hello world!")

number = input('Enter a number between 1 and 10:')
if number <= 10 and number >=1:
   print 'Great'
else:
   print 'Wrong!'


numbers = [1,2,3,4,5,6,7]

print(numbers)

x = [1,2,3]
print(x.pop())
x.reverse()
print(x)

age = 10
assert 0 < age <100
age = -1
#assert 0 < age <100

x = 1
while x <= 100:
   print x
   x +=1
#--------------------
name = ''
while not name or name.isspace():
    name = raw_input('Please enter your name:')
print('Hello.%s!' % name)

