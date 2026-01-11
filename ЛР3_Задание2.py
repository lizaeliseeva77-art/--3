# TODO Напишите функцию find_common_participants
def find_common_participants(group1, group2, separator=','):
    # Разделяем строки на списки участников по заданному разделителю
    participants1 = group1.split(separator)
    participants2 = group2.split(separator)
    # Преобразуем списки в множества
    set1 = set(participants1)
    set2 = set(participants2)
    # Находим пересечение
    common = set1.intersection(set2)
    # Возвращаем отсортированный список
    return sorted(list(common))

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
# Проверяем работу функции с разделителем '|' (отличным от запятой)
common_participants = find_common_participants(
    participants_first_group,
    participants_second_group,
    separator='|')

print("Общие участники:", common_participants)
