# Enter a binary number and convert  it into decimal number.
binary = int(input("Entere your Binary number : "))
decimal_no = 0
i = 0

while(binary != 0):
    remainder = binary%10
    decimal_no = decimal_no + remainder*(2**i)
    binary = binary/10
    i = i + 1

print("The decimal equivalent is ", decimal_no)