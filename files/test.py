f = open('test.txt')
print(f.read())
f.close()

print()

with open('test.txt') as f:
    print(f.read())

print()

with open('test.txt') as f:
    for line in f:
        print(line)