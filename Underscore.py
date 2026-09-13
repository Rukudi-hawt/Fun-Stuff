str_to_edit = input('Input the text that you would like to add underscores to:  ')

# for i in range(0, len(str_to_edit) - 1, 1):
#      if str_to_edit[i] == '':
#           str_to_edit[i] = '_'

str_edited = str_to_edit.replace(' ', '_')

print(str_edited)