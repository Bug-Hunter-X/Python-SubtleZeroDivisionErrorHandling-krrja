def function_with_uncommon_error(x, y):
    if x == 0:
        return y / x  # ZeroDivisionError, but might not be immediately obvious
    else:
        return x / y