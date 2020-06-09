print("Welcome to swap nibbles")

class Swap_nibbles:

    #Variable
    x=0

    #method for swapping nibbles
    def swapping_nibbles(self,x): 
        return ( (x & 0x0F)<<4 | (x & 0xF0)>>4 )

#Object creation
swap_nibble=Swap_nibbles()
x=int(input("Enter number:"))
result=swap_nibble.swapping_nibbles(x)
print(result)




  