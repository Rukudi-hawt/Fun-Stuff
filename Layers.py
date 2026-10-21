x = open(r"C:\Users\rukud\OneDrive\Documents\Fun Stuff\Layers.txt", 'a+')
# x.seek(0)
# print(x.read())
# x.seek(0)
# line = x.read()
# print(line)
# x.seek(0)
# line = x.readline()
# print(line.strip())
x.seek(0)
layers = []
for line in x:
     layers.append(line.strip())

print(layers, '\n')
layer1 = layers[0].split(',')
layer2 = layers[1].split(',')
layer3 = layers[2].split(',')

number = layer1[1]
number = int(number)
print(type(number), number)
print(layer1, '\n', layer2, '\n', layer3)
#x.append('whatever user wants to append')
     