lst = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

lst = [tuple(list(ichki_tuple)[:-1] + [100]) for ichki_tuple in lst]

print(lst)