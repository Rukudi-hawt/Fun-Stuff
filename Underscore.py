str_to_edit = input('Input the text that you would like to add underscores to:  ')

# for i in range(0, len(str_to_edit) - 1, 1):
#      if str_to_edit[i] == '':
#           str_to_edit[i] = '_'

str_to_edit = str_to_edit.replace('?', '')
str_to_edit = str_to_edit.replace(' ', '_')
str_to_edit = str_to_edit.replace("'", "")
str_to_edit = str_to_edit.replace("`", "")
str_to_edit = '#' + str_to_edit


print(str_to_edit)