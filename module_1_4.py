# lesson4
my_string = input('Первая строка Вашей любомой песни: ')
dlina_str = len(my_string) # вычисляю длину стороки для вывода и дальнейшего использования переменной
print('Длина этой сторки', dlina_str)
print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ',''))
print('Песня начинается в буквы:', my_string[0])
print('Последня буква строчки:', my_string[dlina_str-1])
