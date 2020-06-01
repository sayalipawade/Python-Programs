#Function to count letters in string
def get_count(input):
    dict={}
    for index1 in input:
        count=0
        for index2 in input:
            if index1==index2:
                count=count+1
        new_dict={index1:count}
        dict.update(new_dict)
    return dict

#Taking input from user   
name=input("Enter String:")
print(get_count(name))  