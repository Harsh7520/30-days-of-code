s1 = input()
s2 = input()
def binaryToDecimal(binary):
    binary1 = binary
    decimal, i, n = 0, 0, 0
    while (binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary // 10
        i += 1
    return decimal
a = binaryToDecimal(int(s1))
b = binaryToDecimal(int(s2))
c = a+b
bin_c = (bin(c)).replace("0b", "")
print(bin_c)
