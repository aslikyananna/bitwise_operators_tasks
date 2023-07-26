def power_of_two(num):
    if num & num-1 == 0:
        return True
    return False
print(power_of_two(5))
print(power_of_two(8))

def four(num):
    if num & num-1 == 0 and (num-1) % 3 == 0:
        return True
    return False
print(four(5))
print(four(16))

def eight(num):
    if num & num-1 == 0 and (num-1) % 7 == 0:
        return True
    return False
print(eight(5))
print(eight(512))