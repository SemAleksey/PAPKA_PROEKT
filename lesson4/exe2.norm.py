# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


original_list = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]

def sort_to_max(original_list):
    for i in range(len(original_list) - 1) :
        for j in range(len(original_list) - 1) :
            if original_list[j] > original_list[j + 1] :
                original_list[j], original_list[j + 1] = original_list[j + 1], original_list[j]
    return(original_list)
print(sort_to_max(original_list))

