name1 = 'bolaji'
name2 = 'chichi'
name3 = 'praise'

print(name1 == name2)
print(name1 < name2)
print(ord('A'))

print('c' in name3)
sentence = 'i love jesus'

print(f'[{name1:10} {name2: <10}]')
print(f'[{name1:>10}]')
print(f'[{name1:<10}]')
print(f'[{name1:^10}]')
print(name1 * 5)

name4 = '   moh    '
print(len(name4))
name4.strip()
print(name4)

print(name1.upper())
print(name3.capitalize())
print(sentence.title())

print(name3.swapcase())

print(sentence.count('e'))
print(sentence.index('e'))
print(sentence.rindex('e'))
name = input('enter ya name').strip()
if name.isdigit():
    print('valid')
else:
    print('invalid')



print(sentence.replace('e', 'x'))

print(sentence.split())
print(sentence.partition('love'))

names = ['olamide', 'aramide', 'ayomide', 'dayomide']

print("-".join(names))