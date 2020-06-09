print("****Quadratic equations*****")
#import complex module
import cmath

#try except block is added due to divide by zero exception
try:
    #get input from user
    number1=int(input("Enter number1 : "))
    number2=int(input("Enter number2 : "))
    number3=int(input("Enter number3 : "))

    # calculate the discriminant
    delta = (number2**2) - (4*number1*number3)

    # find two solutions
    solution1 = (-number2-cmath.sqrt(delta))/(2*number1)
    solution2 = (-number2+cmath.sqrt(delta))/(2*number1)
    print('The solution are {0} and {1}'.format(solution1,solution2))

except ZeroDivisionError:
    #if any exception occurs then print divide by zero
    print("Divide by zero error !")