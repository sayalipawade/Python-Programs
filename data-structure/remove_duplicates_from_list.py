
#Function to remove duplicates from list
def remove_duplicates(given_list):
    new_list=[]
    for index1 in list:
        if index1 not in new_list:
            new_list.append(index1)
    return(new_list)

#Taking list as input
list=[]
size=int(input("Enter size of list:"))
print("Enter elements:")
for index in range(0,size):
    element=int(input())
    list.append(element)
print(list)
print("After deleting duplicate elements:",remove_duplicates(list))