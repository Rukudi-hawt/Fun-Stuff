# layers = [{'Name' : 'Shale', 'Depth' : '8 m', 'Environment' : 'Shallow marine'}, {'Name' : 'Sandstone', 'Depth' : '12 m', 'Environment' : 'River'}, {'Name' : 'Limestone', 'Depth' : '5 m', 'Environment' : 'Shallow marine'}]

# print('STRATIGRAPHIC COLUMN\n', '___________________________________________________________\n')

# for i in range(0, len(layers), 1):
#      dctIndex = layers[i]
#      strDisplay = ''
#      strDisplay =   f'{dctIndex.get('Name')} {dctIndex.get('Depth')} {dctIndex.get('Environment')}'
#      print('Layer ', str(i), ': ', strDisplay) 

def display_layers(names, depths, environments):
     print('STRATIGRAPHIC COLUMN\n', '_' * 67, '\n')
     for i in range(0, len(names), 1):
           str_display = names[i] + '   ' + str(depths[i]) + '   ' + environments[i]
           print("Layer ", str(i + 1), ': ', str_display, '\n')

thickness = []
def calculate_thickness(depths):
     for i in range(0, len(depths) - 1, 1):
           int_thickness = int(depths[i]) - int(depths[i+1])
           thickness.append(int_thickness)
     thickness.append(int(depth[-1]))

def count_type(types):
      unique_types = list(set(types))

      for i in unique_types:
          print(f'{i}: {types.count(i)}')
      print('\n')
def depositional_event (layer_name, layer_environment, thickness_size):
     layer_name = input('Insert the rock type: ', )
     layer_environment = input('Insert the environment type: ', )
     thickness_size = int(input('Insert the thickness of the layer: ', ))

     layer_name = layer_name.rstrip(' ')
     layer_name = layer_name.replace(' ', '_')

     name.append(layer_name)
     environment.append(layer_environment)
     thickness.append(thickness_size)

     # for i in depth:
     #       i = i + thickness_size
     depth = [i + thickness_size for i in depth]

#probably going to have to move this to after erosion file opened and populated erosion_history list
erosion_history = []
def erosion_event (total_erosion):
      total_erosion = int(input('Input the total amount of erosion experienced: ',))
      if total_erosion < thickness:
          thickness[-1] = thickness[-1] - total_erosion
      else:
          del thickness[-1]
     #what if the erosion is big enough to remove more than 1 layer's thickness
      
      depth = [i - total_erosion for i in depth] 
      for i in range(0, len(depth), 1):
            if depth[i] <= 0:
                  del depth[i]
                  del name[i]
                  del environment[i]

txt_layers = open(r"C:\Users\rukud\OneDrive\Documents\Fun Stuff\Layers.txt", 'r+')

txt_layers.seek(0)
layers = []
for line in txt_layers:
     layers.append(line.strip())

name = []
depth = []
environment = []

for i in range(0, len(layers), 1):
     store = layers[i].split(',')
     name.append(store[0])
     depth.append(store[1])
     environment.append(store[2])

if input('Would you like to add a new layer: Y/N\n',).capitalize() == 'Y':
     new_name = (input('Layer name: ',)).capitalize()
     new_depth = (input('Layer depth: ',))
     new_environment = (input('Layer environment: ',)).capitalize()

     if '' in new_name: 
          new_name.replace('', '_')

     if '' in new_environment:
               new_environment.replace('', '_')

     name.append(new_name)
     depth.append(new_depth)
     environment.append(new_environment)

for inner in range(0, (len(depth)), 1):
          for outer in range(1, len(depth), 1):
               if depth[inner] > depth[outer]:
                    temp = depth[inner]
                    depth[inner] = depth[outer]
                    depth[outer] = temp

                    temp = name[inner]
                    name[inner] = name[outer]
                    name[outer] = temp

                    temp = environment[inner]
                    environment[inner] = environment[outer]
                    environment[outer] = temp

new_layer = name[-1] + ',' + depth[-1] + ',' + environment[-1]
txt_layers.truncate(0)
txt_layers.seek(0)
for i in range(0, len(name), 1):
     line = name[i] + ',' + str(depth[i]) + ',' + environment[i]
     if i >= 1: 
          txt_layers.write(f'\n{line}')
     else:
          txt_layers.write(f'{line}')

display_layers(name, depth, environment)
calculate_thickness(depth)
print(f'Thicknesses of the layers:\n {'_' * 67}\n')
for i in thickness:
      print(f'Layer {thickness.index(i) + 1}:    {i}m')
print(f'The thickest layer is {name[thickness.index(max(thickness))]} ({max(thickness)}m thick)\n')
count_type(name)

txt_layers.close()