import math
from heapq import heappush, heappop


arr = []
def heapsort():
    """
    Основная функция для сортировки массива заданного размера используя алгоритм heapsort
    """
    global arr
    h = []
    # построение кучи
    for value in arr:
        heappush(h, value)
    arr = []
    # извлечение отсортированных элементов один за другим
    arr = arr + [heappop(h) for _ in range(len(h))]


def InsertionSort(begin, end):
    """
    Основная функция сортировки данных с использованием алгоритма сортировки вставкой
    """
    left = begin
    right = end
    # Пройти от 1 до len
    for i in range(left + 1, right + 1):
        key = arr[i]
        # Переместить элементы arr [0..i-1], которые
        # больше ключа, на одну позицию вперед и № их текущей позиции
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j = j - 1
        arr[j + 1] = key


def Partition(low, high):
    """
    Эта функция принимает последний элемент в качестве точки, мест
    элемент поворота в правильном положении в отсортированном
    массив, и все места меньше (меньше, чем сводная)
    слева от точки поворота и всех больших элементов справа
    Количество точек разворота
    """
    global arr
    # пивот
    pivot = arr[high]
    # индекс меньшего элемента
    i = low - 1
    for j in range(low, high):
        # Если текущий элемент меньше или равен оси вращения
        if arr[j] <= pivot:
            # индекс приращения меньшего элемента
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])
    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])
    return i + 1


def MedianOfThree(a, b, d):
    """
    Функция найти медиану из трех элементов в индексе a, b, d
    """
    global arr
    A = arr[a]
    B = arr[b]
    C = arr[d]
    if A <= B <= C:
        return b
    if C <= B <= A:
        return b
    if B <= A <= C:
        return a
    if C <= A <= B:
        return a
    if B <= C <= A:
        return d
    if A <= C <= B:
        return d


def IntrosortUtil(begin, end, depth_limit):
    """
    Основная функция, которая реализует Introsort
    low -> Начальный индекс,
    high -> Конечный индекс
    deepLimit -> уровень рекурсии
    """
    global arr
    size = end - begin
    if size < 16:
        # если набор данных небольшой, вставить сортировку вызовов
        InsertionSort(begin, end)
        return
    if depth_limit == 0:
        # если предел рекурсии достигнут, вызовите сортировку кучи
        heapsort()
        return
    pivot = MedianOfThree(begin, begin + size // 2, end)
    (arr[pivot], arr[end]) = (arr[end], arr[pivot])
    # partitionPoint - разделительный индекс, arr [partitionPoint] теперь в нужном месте
    partitionPoint = Partition(begin, end)
    # Отдельно сортировать элементы перед разделом и после раздела
    IntrosortUtil(begin, partitionPoint - 1, depth_limit - 1)
    IntrosortUtil(partitionPoint + 1, end, depth_limit - 1)


# Сервисная функция для запуска модуля Introsort
def Introsort(begin, end):
    # инициализировать глубину Limit как 2 * log (длина (данные))
    depthLimit = 2 * math.log2(end - begin)
    IntrosortUtil(begin, end, depthLimit)


# Печать данных массива
def printArr():
    print('Arr: ', arr)


def main():
    global arr
    # arr = arr + [
    #     2, 10, 24, 2, 10, 11, 27,
    #     4, 2, 4, 28, 16, 9, 8,
    #     28, 10, 13, 24, 22, 28,
    #     0, 13, 27, 13, 3, 23,
    #     18, 22, 8, 8]
    # n = len(arr)
    # Introsort(0, n - 1)
    # printArr()


if __name__ == '__main__':
    main()
