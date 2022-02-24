def multiply_result(sign: str):
    def foo(function):
        def decoratee():
            multiply_var = sign * 10
            return f"{multiply_var}\n{function()}"
        return decoratee
    return foo




@multiply_result("++++")
def multiply(x, y):
    return x * y
num1 = 10
num2 = 2

print(multiply(num1, num2))
