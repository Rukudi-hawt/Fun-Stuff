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

print('WELCOME TO PORTUGUES LESSONS FOR GRINGOS!\nWhad would you like to do today?')
str_what_to_do = input('Practice/Add:    ', )
 
lst_verbos = str_verbos.splitlines()
lst_verbos_pair = []
lst_ar_portugues = []
lst_er_portugues = []
lst_ir_portugues = []
lst_ar_translation = []
lst_er_translation = []
lst_ir_translation = []
str_answer = ''

while str_what_to_do.capitalize() == 'Add':
     str_portugues_add = input('Please type in your Portugues verb:   ',)
     if 'ar' or 'ir' or 'er' in str_portugues_add[len(str_portugues_add) - 2: len(str_portugues_add)]:
          str_ingles_add = input('Please type in your English verb:   ',)
          str_verbos += '\n' + str_portugues_add + '\n' + str_ingles_add
     if input('Would you like to practice? Y/N:   ',) == 'Y':
            str_what_to_do2 = 'Practice'
            break


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

if str_what_to_do.capitalize() or str_what_to_do2.capitalize() == 'Practice':
     for i in range(0, len(lst_ar_portugues), 2):

                    bl_next = False
                    while bl_next == False:
                         print('What does this word translate to:     ', lst_ar_portugues[i])
                         str_ingles_reposta = str(lst_ar_translation[i])
                         str_answer = input('Type your answer here:   ',)

                         if str_ingles_reposta.capitalize() != str_answer.capitalize():
                                   print('Err-orr! Nao nao nao, irmao. E reposta nao esta correta!')
                                   str_continue = input('Would you like to continue?\nY/N:     ',)
                                   if str_continue == 'Y' or 'Yes':
                                        print('Here you go. Tenta de novo, meu amigo!')
                                   else:
                                        break
                         else:
                              print('Correta, irmao!')
                              str_answer = input('Would you like to continue?\nY/N:  ',)  
                              if str_answer.capitalize() == 'Y' or 'Yes':
                                       print('Here you go. Tenta de novo, meu amigo!')
                                       bl_next = True
                              else:
                                   print('\nTchau, amigo. Lembre-se: a word a day keeps the forgetfulness away.')
                                   break       


#     print(lst_ar_translation[lst_ar_portugues[1].index])