def num_ceil(x):
    int_part = int(x)
    if x > 0 and x != int_part:
        return int_part + 1
    else:
        return int_part

print(num_ceil(3.141592))
print(num_ceil(3.0000000001))
print(num_ceil(-1.1))