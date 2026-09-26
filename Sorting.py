lst_numbers = [5, 2, 9, 1, 6]

for i in range(0, len(lst_numbers) - 1, 1):
     int_comparison = int(lst_numbers[i])
     # if lst_numbers[i-1] > lst_numbers[i]:
     #      temp = lst_numbers[i]
     #      lst_numbers[i] = lst_numbers[i-1]
     #      lst_numbers[i-1] = temp
     if i != len(lst_numbers) - 1:
          for x in range(i + 1, len(lst_numbers) - 1, 1):
               if int_comparison > lst_numbers[x]:
                    index = lst_numbers.index(int_comparison)
                    temp = lst_numbers[x]
                    lst_numbers[x] = int_comparison
                    lst_numbers[index] = temp 

print(lst_numbers)
          