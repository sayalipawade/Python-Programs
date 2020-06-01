#Sum of element in list
def sum_of_element(given_list):
    sum=0
    for index in given_list:
        sum=sum+index
    print("Sum of element in the list:",sum)

#list 
list=[1,2,3,4,5,6,8]
print(list)
sum_of_element(list)