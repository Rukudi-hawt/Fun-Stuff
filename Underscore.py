str_to_edit = input('Input the text that you would like to add underscores to:  ')

# for i in range(0, len(str_to_edit) - 1, 1):
#      if str_to_edit[i] == '':
#           str_to_edit[i] = '_'

#need to create a loop that accounts for pretty much ALL special characters and punctuation within the string
#Do I have to have a while loop to keep my programme running indefinetely?

lst_chars = [
    '~', '?', '<', '>', ']', '{', '}', '}', '!', '@', 
    '$', '%', '^', '*', '&', '(', ')', ')', '*', '+', 
    '`', "'", '"', ':']

for x in lst_chars:
     if x in str_to_edit:
          str_to_edit = str_to_edit.replace(x, '_')

if '#' in str_to_edit and str_to_edit[1] == '#':
     str_to_edit = str_to_edit
elif '#' in str_to_edit and str_to_edit[1] != '#':
     str_to_edit = str_to_edit.replace('#', '')
     str_to_edit = '#' + str_to_edit
else:
     str_to_edit = '#' + str_to_edit

str_to_edit = str_to_edit.replace(' ', '_')

print(str_to_edit)