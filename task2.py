"""
Задание 2.
Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
Используйте форматирование строк.
Пример:
Введите время в секундах: 3600
Время в формате ч:м:с - 1.0 : 60.0 : 3600
"""
second = int(input('Введите время в секундах: '))
minut = int(second / 60)
second = second - (minut * 60)
hours = int(minut / 60)
minut = minut - (hours * 60)
print(f'Время в формате ч:м:с - {float(hours)} : {minut} : {second}')
