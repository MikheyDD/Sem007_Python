# Задача №51. Решение в группах
# Напишите функцию same_by(characteristic, objects), которая
# проверяет, все ли объекты имеют одинаковое значение
# некоторой характеристики, и возвращают True, если это так.
# Если значение характеристики для разных объектов
# отличается - то False. Для пустого набора объектов, функция
# должна возвращать True. Аргумент characteristic - это
# функция, которая принимает объект и вычисляет его
# характеристику.
# Ввод: 
# values = [0, 2, 10, 6] 
# if same_by(lambda x: x % 2, values):
# print(‘same’)
# else:
# print(‘different’)

# Вывод:
# same

values = [0, 2, 10, 6] 


# def same_by(characteristic, objects):
#     res = []
#     for obj in objects:
#         res.append(characteristic(obj))
#     return not all(res)


# # print(same_by(lambda x: x % 2, values))

# if same_by(lambda x: x % 2, values):
#     print('same')
# else:
#     print('different')



def same_by(characteristic, objects: list):
    char_compare = characteristic(objects[0])  
     # находим значение хар-ки первого эл-та
    # сравниваем значения хар-к всех эл-тов
    result_list = list(map(lambda x: characteristic(x) == char_compare, objects))
    if len(objects) == 0:
        return True
    return all(result_list)

if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')



