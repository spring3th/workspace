words = ['this','is','an','ex','parrot']
for word in words:
    print(word)
numbers = [1,2,3,4,5,6,7,8,9]
for number in numbers:
    print number
print(range(10))

for number in range(1,10):
    print number

d = {'x':1,'y':2,'z':3}
for key in d:
    print(key , 'corresponds to',d[key])

names = ['name','beth','george','damon']
ages = [12,45,32,102]

print(zip(names,ages))
for name,age in zip(names,ages):
    print name,'is',age,'years old'

for i in range(len(names)):
    print(names[i],'is',ages[i],'years old')


