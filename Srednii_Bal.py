grades = [[5,3,3,5,4],[2,2,2,3],[4,5,5,2],[4,4,3],[5,5,5,4,5]] # создаём список из оценок
students = {'Johnny','Bilbo','Steve', 'Khendrik', 'Aaron'} # создаем множество из имён
tuple_data = tuple(students) # преобразуем множество в кортеж
sorted_list = sorted (tuple_data) # сортируем в алфавитном порядке кортеж

a=sum(grades[0]) # Вычисляем среднее арифметическое 1 ученика
b=len(grades[0])
sr_arifm1=a/b

a=sum(grades[1]) # Вычисляем среднее арифметическое 2 ученика
b=len(grades[1])
sr_arifm2=a/b

a=sum(grades[2]) # Вычисляем среднее арифметическое 3 ученика
b=len(grades[2])
sr_arifm3=a/b

a=sum(grades[3]) # Вычисляем среднее арифметическое 4 ученика
b=len(grades[3])
sr_arifm4=a/b

a=sum(grades[4]) # Вычисляем среднее арифметическое 5 ученика
b=len(grades[4])
sr_arifm5=a/b

srednii_bal={sorted_list[0]:sr_arifm1, # Создаём словарь
             sorted_list[1]:sr_arifm2,
             sorted_list[2]:sr_arifm3,
             sorted_list[3]:sr_arifm4,
             sorted_list[4]:sr_arifm5}

print(srednii_bal)