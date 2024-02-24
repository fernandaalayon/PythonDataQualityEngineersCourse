import random
from statistics import mean


def create_list() -> list:
    list_number = []
    for number in range(100):  # For to populate the list
        list_number.append(random.randint(1, 100))  # Adding random values to the list
    return list_number


def sort_list_min_max(list_numbers: list):
    n: int = len(list_numbers)

    for i in range(n - 1):
        for j in range(n - 1):
            if list_numbers[j] > list_numbers[j + 1]:  # Compare the actual index value with the next to get the minor
                temp = list_numbers[j + 1]  # Adding the minor value to temp
                list_numbers[j + 1] = list_numbers[j]  # Adding the greater value to the next index
                list_numbers[j] = temp  # Adding the temp value to the current index
    return list_numbers


def get_average_even_numbers(list_numbers: list) -> float:
    list_even_numbers = []  # New list dedicated to even numbers
    for number in list_numbers:  # Iteration to get all even numbers
        if number % 2 == 0:
            list_even_numbers.append(number)  # Adding even number to even numbers list
    print('Even numbers: ', list_even_numbers)
    return sum(list_even_numbers) / len(list_even_numbers)  # returning the average


def get_average_odd_numbers(list_numbers: list) -> int:
    list_odd_numbers = []  # New list dedicated to odd numbers
    for number in list_numbers: # Iteration to get all odd numbers
        if number % 2 != 0:
            list_odd_numbers.append(number)  # Adding even number to even numbers list
    print('Odd numbers: ', list_odd_numbers)
    return mean(list_odd_numbers)  # Returning the average implementing mean function


if __name__ == '__main__':
    list_numbers_definition = create_list()
    print('Initial LIST: ', list_numbers_definition)
    sort_list_min_max(list_numbers_definition)
    print('Sorted LIST: ', list_numbers_definition)
    print('Even number average: ', get_average_even_numbers(list_numbers_definition))
    print('Odd number average: ', get_average_odd_numbers(list_numbers_definition))
