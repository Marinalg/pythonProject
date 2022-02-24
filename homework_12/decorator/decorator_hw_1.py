from typing import Callable

def print_name(decorated_function: Callable):
    def decoratee():
        name = "Сумма чисел"
        return f"{name}\n{sum_numbers()}"
    return decoratee

@print_name
def sum_numbers(numbers: int):
        total = 0
        for number in numbers:
            total += number
        return total
sum_numbers([1, 2, 3, 4, 5])

print(sum_numbers())


