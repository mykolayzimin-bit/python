
# Task 1
# Write a decorator that prints a function with arguments passed to it.

def logger(func):
    def wrapper(*args):
        print(f"{func.__name__} called with {', '.join(str(x) for x in args)}")
        return(func(*args))
    return wrapper

@logger
def add(x, y):
    return x + y

@logger
def square_all(*args):
    return [arg ** 2 for arg in args]

result = add(4, 5)
result = square_all(4, 5)

# Task 2
# Write a decorator that takes a list of stop words and replaces them with * inside the decorated function

def stop_words(words: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in words:
                result = result.replace(word, '*')
            return result
        return wrapper
    return decorator

@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan("Steve") == "Steve drinks * in his brand new *!"
print("Everything goes right!")

# Task 3
# Write a decorator 'arg_rules' that validates arguments passed to the function.

def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(argument, *args, **kwargs):
            
            if not isinstance(argument, type_):
                print(f"Failed: Argument type must be {type_.__name__}")
                return False
            
            if len(argument) > max_length:
                print(f"Failed: Argument length exceeds {max_length}")
                return False
            
            for symbol in contains:
                if symbol not in argument:
                    print(f"Failed: Argument must contain '{symbol}'")
                    return False
            
            return func(argument, *args, **kwargs)
            
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

assert create_slogan('johndoe05@gmail.com') is False

assert create_slogan('S@SH05') == 'S@SH05 drinks pepsi in his brand new BMW!'

print("All tests are successfully passed!")
