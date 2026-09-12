str_verbos = '''falar
speak
comer
eat
beber
drink
durmir
sleep
respirar
breathe'''

# print('WELCOME TO PORTUGUES LESSONS FOR GRINGOS!\nWhad would you like to do today?')
# str_what_to_do = input('Practice/Add:    ', )

# if str_what_to_do.capitalize() == 'Add':
#      str_portugues_add = input('Please type in your Portugues verb:  ',)
#      if 'ar' or 'ir' or 'er' in str_portugues_add[len(str_portugues_add) - 2: len(str_portugues_add)]:
#           str_ingles_add = input('Please type in your English verb:  ',)
#           str_verbos += '\n' + str_portugues_add + '\n' + str_ingles_add
 
#if str_what_to_do.capitalize() == 'Practice':

lst_verbos = str_verbos.splitlines()
lst_verbos_pair = []
lst_ar_portugues = []
lst_er_portugues = []
lst_ir_portugues = []
lst_ar_translation = []
lst_er_translation = []
lst_ir_translation = []

for i in range(0, len(lst_verbos) - 1, 2):
     lst_verbos_pair.append([lst_verbos[i], lst_verbos[i+1]])

     
     temp_string = str(lst_verbos[i])
     if 'ar' in temp_string[len(temp_string) - 2: len(temp_string)]:
          lst_ar_portugues.append(lst_verbos[i])
          lst_ar_translation.append(lst_verbos[i+1])

     if 'er' in temp_string[len(temp_string) - 2: len(temp_string)]:
               lst_er_portugues.append(lst_verbos[i])
               lst_er_translation.append(lst_verbos[i+1]) 

     if 'ir' in temp_string[len(temp_string) - 2: len(temp_string)]:
          lst_ir_portugues.append(lst_verbos[i])   
          lst_ir_translation.append(lst_verbos[i+1])

     # for i in lst_ar_portugues:
     #       print('What does this word translate to: ', i)
     #       str_answer = lst_ar_translation[lst_ar_portugues.index]

     print(lst_ar_translation[lst_ar_portugues[1].index])