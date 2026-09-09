str_verbos = '''falar, speak
comer
eat
beber
drink
durmir
sleep
respirar
breathe
gostata
like'''

lst_verbos = str_verbos.splitlines()
lst_verbos_pair = []

for i in range(0, len(lst_verbos), 1):
     lst_verbos_pair.append(lst_verbos[i])
     lst_verbos_pair.append(lst_verbos[i+1])

print(lst_verbos_pair)