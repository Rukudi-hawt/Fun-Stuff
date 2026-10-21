layers = [{'Name' : 'Shale', 'Depth' : '8 m', 'Environment' : 'Shallow marine'}, {'Name' : 'Sandstone', 'Depth' : '12 m', 'Environment' : 'River'}, {'Name' : 'Limestone', 'Depth' : '5 m', 'Environment' : 'Shallow marine'}]

print('STRATAGRAPHIC COLUMN\n', '___________________________________________________________\n')

for i in range(0, len(layers), 1):
     dctIndex = layers[i]
     strDisplay = ''
     strDisplay =   f'{dctIndex.get('Name')} {dctIndex.get('Depth')} {dctIndex.get('Environment')}'
     print('Layer ', str(i), ': ', strDisplay)
