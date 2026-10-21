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
     print(layers)
     