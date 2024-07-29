def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    iterations = 0  # Лічильник ітерацій
    upper_bound = None  # Верхня межа

    while low <= high:
        iterations += 1  # Збільшуємо кількість ітерацій
        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
            upper_bound = arr[mid] if upper_bound is None or arr[mid] < upper_bound else upper_bound
        else:
            return (iterations, arr[mid])

    if upper_bound is None and low < len(arr):
        upper_bound = arr[low]

    return (iterations, upper_bound)

# Тестуємо функцію бінарного пошуку
arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
x = 5.0

print(binary_search(arr, x))  # Виведе: (4, 5.5)
