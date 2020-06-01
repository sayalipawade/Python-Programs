#Function to check the unique value in dictionary
def check_unique_value(given_dict):
    list=[]
    for index1,index2 in dict1.items():
        if index2 not in list:
            list.append(index2)
    print("Unique values:",list)

#Dictionary
dict1={1:"sayali",2:"pooja",3:"prapti",4:"kiran",5:"pooja",6:"sayali"}
print(dict1)
check_unique_value(dict1)