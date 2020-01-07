def max(a, b):
    if a > b:
        return a
    else:
        return b

a = max(1,3)
print(a)

b = 'ab'
# None
def f():
    pass

x = 4
y = '4'

print(x==y)

x,y,z = 1,2,3
x=y=z=1

x = 'a'
y = 'b'
z = x + y
print(z)

a = 1.0
a = [1,2,3,'a', x] # list
c = a + [[1,2]]
print(c)
b = (1,2,3,'a',x) # tuple
# b[0] = 1

print(a==tuple(list(b)))
print(range(10))

for i in range(2, 10, 2):
    print(i)

a = {
    'a': 1,
    'b': 'c'
}

print(a['a'])
a = {1,2,1}
print(a)

a = True
a = False

a = b'abc'
print(a)

print(type(list()))

x = str('a')
x = str(1)
x = int(2)
x = int('2')
x = float('2.5')
x = dict(name='John', age=36)
print(x['name'])

x = 1j

a = '0123456789'
print(a[-3:-1])

a = '  ABC,def  '
print(a.strip())
print(a.lower())
print(a.upper())
print(a.replace('A', 'T'))
print(a.split(','))
print(',' in a)
print(':' not in a)

a = 1
if a < 5 and a > 3: pass
if 1 < a < 3: pass
if not a:
    pass

if int is not type(a): print(1)

a = [1,2,3,4,5]
b = [x*2 for x in a if x%2 == 0]
print(b)

if 1 in a:
    print(1)

a.append(6)
print(a)
a.remove(5)
b = list(a)
#a.clear()
print(b)

if 0: print(0)
else: print(1)

for x in range(len(a)):
    print(a[x])

x = 0
while x < len(a):
    print(a[x])
    x += 1


def func1(var1:int, var2:int=2) -> int:
    x = lambda var1,var2 : var1+var2
    return x

b = func1(var2=100, var1=200)
print(b(1,2))
