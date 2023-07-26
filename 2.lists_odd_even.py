def lists_odd_even(ls):
    list_odd = []
    list_even = []
    for i in list:
        if i & 1 == 1:
            list_odd.append(i)
        else:
            list_even.append(i)
    return "list_odd is", list_odd, \
        "list_even is", list_even

ls = [1,3,4,5,6]
print(lists_odd_even(ls))