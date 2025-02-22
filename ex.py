import sys
import functools
def conditional_call(condition):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if condition:
                return func(*args, **kwargs)
            else:
                print(f"Skipping {func.__name__} because condition is not met")
        return wrapper
    return decorator

# 假设我们通过命令行参数控制是否运行某个函数
run_function = "--run" in sys.argv

@conditional_call(run_function)
def example_function():
    print("Function is running!")

example_function()