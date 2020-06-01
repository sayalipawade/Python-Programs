#Delete element from set
def discard_element(set1):
    element1=int(input('Enter element to be deleted:'))
    set1.discard(element1)
    return(set1)

#Taking input from user
set1=set()
size=int(input('Enter size of set:'))
print("Enter elements:")
for index in range(0,size):
    element=int(input())
    set1.add(element)
print("After deleting element from set:",discard_element(set1))

