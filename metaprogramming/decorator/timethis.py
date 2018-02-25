import time
from functools import wraps


def timethis(func):

    @wraps(func) # Very important annotation. Without this annotation function metadata will be lost!
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper

@timethis
def countdown(n:int) -> None:
    '''
    Count to zero

    '''

    while n > 0:
        n -= 1

if __name__ == '__main__':
    countdown(10000)

    # Metadata
    print(countdown.__name__)
    print(countdown.__doc__)
    print(countdown.__annotations__)