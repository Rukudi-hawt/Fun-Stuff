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

name = []
depth = []
environment = []

for i in range(0, len(layers), 1):
     store = layers[i].split(',')
     print(store)
     name.append(store[0])
     depth.append(store[1])
     environment.append(store[2])

print(name, '\n', depth, '\n', environment)

if input('Would you like to add a new layer: Y/N\n',).capitalize() == 'Y':
     new_name = (input('Layer name: ',)).capitalize
     new_depth = (input('Layer depth: ',))
     new_environment = (input('Layer environment: ',)).capitalize

     if ' ' in new_name:
          new_name.replace(' ', '_')

     if ' ' in new_environment:
               new_environment.replace(' ', '_')

     name.append(new_name)
     depth.append(new_depth)
     environment.append(new_environment)

     new_layer = name[-1] + ',' + depth[-1] + ',' + environment[-1]
     x.write(new_layer)

# print(layers, '\n') 
# layer1 = layers[0].split(',')
# layer2 = layers[1].split(',')
# layer3 = layers[2].split(',')

# number = layer1[1]
# number = int(number)
# print(type(number), number)
# print(layer1, '\n', layer2, '\n', layer3)
#x.append('whatever user wants to append')
     