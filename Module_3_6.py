# Что должно быть подсчитано:
#
# Все числа (не важно, являются они ключами или значениям или ещё чем-то).
# Все строки (не важно, являются они ключами или значениям или ещё чем-то)
#
#
# Для примера, указанного выше, расчёт вёлся следующим образом:
#
# 1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99




data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])]

print(type(data_structure))

def calculate_structure_sum(data_structure):
    pass


result = calculate_structure_sum(data_structure)

print(result)