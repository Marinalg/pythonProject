import time
import math


def time_of_function(function):
    def wrapped(numbers:int):
        start_time = time.perf_counter_ns()
        result = function(numbers)
        print(time.perf_counter_ns() - start_time)
        return result

    return wrapped

@time_of_function
def square_root():
    result = []
    for number in numbers:
        result.append(math.sqrt(number))
    return result
numbers = [4, 9, 16, 36]
print(square_root(numbers))