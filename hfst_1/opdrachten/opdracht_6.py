# Open lied.txt in Python
lied = open("<hfst_1\opdrachten\lied.txt", "r")
# Vorm lied om naar lijst, vervang witregels '\n' door spaties ' ' 
lied = lied.read().replace('\n', ' ') 
# Test inhoud van lied
print(lied)

""" Begin eigen code hier """

dict = {}
for woord in lied.split():
    if woord not in dict:
        dict[woord] = 1
    else:
        dict[woord] += 1

print(dict)