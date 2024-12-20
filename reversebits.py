def reverse_bits(num):
# Find the bit length of the number
    bit_length = num.bit_length()
    reversed_num = 0
    for i in range(bit_length):
# Extract the least significant bit of the number
        bit = (num >> i) & 1
# Place this bit in the reversed number at the correct position
        reversed_num |= (bit << (bit_length - 1 - i))
    return reversed_num
 
num = int(input("Enter a number: "))
print(reverse_bits(num))