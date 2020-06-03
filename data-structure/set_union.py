#Union of two sets
def union_of_set(set1,set2):
    new_set=set()
    for index1 in set1:
        new_set.add(index1)
    for index2 in set2:
        if index2 not in set1:
            new_set.add(index2)
    return new_set

# Two sets
set1={11,44,88,66,22}
set2={11,22,33}
print(union_of_set(set1,set2))

