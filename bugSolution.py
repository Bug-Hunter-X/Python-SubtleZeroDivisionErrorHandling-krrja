def function_with_uncommon_error(x, y):
    if x == 0 or y == 0:
        return float('inf') # Or raise a custom exception or return a different default value
    else:
        return x / y