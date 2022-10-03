""" Niveau 1"""
dict_1={1: 10, 2: 20}
dict_2={3: 30, 4: 40}
dict_3={5: 50, 6: 60}
# Resultaat: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dict_1.update(dict_2)
dict_1.update(dict_3)
print(dict_1)

""" Niveau 2 """
dict = {'a': 'Red', 'b': 'Green', 'c': None}
# Resultaat: {'a': 'Red', 'b': 'Green'}
for key, value in dict.items():
    if not value:
        del dict[key]
        break
print(dict)

""" Niveau 3 """
dict_1 = {'a': 100, 'b': 200, 'c':300}
dict_2 = {'a': 300, 'b': 200, 'd':400}
# Resultaat: {'a': 400, 'b': 400, 'd': 400, 'c': 300})

dict_ni = {}
for key, value in dict_1.items():
    if key not in  dict_ni:
        dict_ni[key] = value
    else:
        dict_ni[key] += value
for key, value in dict_2.items():
    if key not in  dict_ni:
        dict_ni[key] = value
    else:
        dict_ni[key] += value
print(dict_ni)
