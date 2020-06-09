print("Welcome to swap nibbles")

class Swap_nibbles:

    #Variable
    number=0

    #method for swapping nibbles
    def swapping_nibbles(self,number): 
        return ( (number & 0x0F)<<4 | (number & 0xF0)>>4 )

#Object creation
swap_nibble=Swap_nibbles()
number=int(input("Enter number:"))
result=swap_nibble.swapping_nibbles(number)
print("After swapping nibbles number is:",result)