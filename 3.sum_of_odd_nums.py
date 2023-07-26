
def sum_of_odd_nums(ls):
    sum = 0
    for i in ls:
        if i & 1 == 1:
            sum += i
        else:
            continue
    return sum
ls = [1,3,4,5,6]
print(sum_of_odd_nums(ls))
