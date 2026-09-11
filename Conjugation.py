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

print(lst_er_portugues, ';', lst_ir_portugues, ';', lst_ar_portugues)


