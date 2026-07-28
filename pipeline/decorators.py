import time
import functools


# timer decorator
def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.perf_counter() - start:.4f}s")
        return result

    return wrapper


# log calls
def log_calls(target_list):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            target_list.append(
                {
                    "name": func.__name__,
                    "args": args,
                    "result": result,
                }
            )
            return result

        return wrapper

    return decorator
