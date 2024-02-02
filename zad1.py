def validate_int_args(func):
    def wrapper(*args, **kwargs):
        # Sprawdź, czy wszystkie argumenty są liczbami całkowitymi
        if all(isinstance(arg, int) for arg in args):
            return func(*args, **kwargs)
        else:
            print("Invalid arguments, only integers allowed!")

    return wrapper

@validate_int_args
def multiply_numbers(a, b):
    return a * b

print(multiply_numbers(5, 6))  # Output: 30
print(multiply_numbers("abc", 3))  # Output: Invalid arguments, only integers allowed! 

#(nie wiem  czy to jest dobrze bo dla mnie zaczynają sie robić schody,że tak powiem) 