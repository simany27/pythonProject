array_input = list(set(map(int, input("Введите числа через пробел: ").split())))
element_input = int(input("Введите любое число: "))


def sort_bubble(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находим середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


sort_bubble(array_input)
index = None

if element_input <= array_input[0] or element_input >= array_input[-1]:
    print("Нет числа, которое меньше/больше введенного")
elif element_input in array_input:
    index = binary_search(array_input, element_input, 0, len(array_input) - 1)
else:
    while not index:
        element_input += 1
        index = binary_search(array_input, element_input, 0, len(array_input) - 1)

if index:
    print(f"Индекс элемента, который меньше введенного числа: {index-1}")
    print(f"Индекс элемента, больше него, или равного: {index}")
