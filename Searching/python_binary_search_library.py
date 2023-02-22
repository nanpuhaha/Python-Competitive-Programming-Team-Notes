from bisect import bisect_left, bisect_right

# Locate the leftmost value exactly equal to x
def index_of_x(a, x):
    i = bisect_left(a, x)
    return i if i != len(a) and a[i] == x else None

# Locate the rightmost value less than x
def index_of_less_than_x(a, x):
    return i - 1 if (i := bisect_left(a, x)) else None

# Locate the rightmost value less than or equal to x
def index_of_less_or_equal_than_x(a, x):
    return i - 1 if (i := bisect_right(a, x)) else None

# Locate the leftmost value greater than x
def index_of_greater_than_x(a, x):
    i = bisect_right(a, x)
    return i if i != len(a) else None

# Locate the leftmost value greater than or equal to x
def index_of_greater_equal_than_x(a, x):
    i = bisect_left(a, x)
    return i if i != len(a) else None

n = 10
target = 13
array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

result = index_of_x(array, target)
if result is None:
    print(None)
else:
    print(result + 1)
