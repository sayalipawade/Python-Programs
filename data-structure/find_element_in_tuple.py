#Function to find element in tuple
def search_fruit_tuple(search_fruit):
    flag=0
    for index1 in fruit:
        if search_fruit == index1:
            flag=1
            break
    if flag == 1:
        print("Fruit found")
    else:
        print("Fruit not found")

#Tuple
fruit=("Apple","mango","banana","grapes")
search_fruit="mango"
search_fruit_tuple(search_fruit)