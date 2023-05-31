"""
Bepaal recursief de som van alle elementen in een lijst.
De lijst bestaat uit veel verschillende niveau's.
"""

print( som_lijst([1,2,3,4]) )           # 10
print( som_lijst([1, [2,3], 4]) )       # 10
print( som_lijst([1,2,[3,[4]]]) )       # 10
print( som_lijst([1, [2, [3, [4]]]]) )  # 10
