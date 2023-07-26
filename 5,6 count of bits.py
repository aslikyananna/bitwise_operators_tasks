def count_of_bits(num):
    count = 0
    while num != 0:
        if num & 1 == 1:
            count += 1
        num = num >> 1
    return count


def count_with_modulo(num):
    count = 0
    while num != 0:
        count += 1
        num = num >> 1
    return count

print(count_of_bits(7))
print(count_with_modulo(7))