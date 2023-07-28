def digit(n) :
    Digit = n % 10
    return Digit
def tens(n) :
    n = n // 10
    Tens = n % 10
    return Tens
def hundreds(n) :
    n = n // 10
    n = n // 10
    Hundreds = n % 10
    return Hundreds
def thousands(n) :
    Thousands = n // 1000
    return Thousands
def sum_digits(n) :
    sum_digits = digit(n) + tens(n) + hundreds(n) + thousands(n)
    return sum_digits
n   = int(input('Enter a number (0 to 9999): '))
print('Digit place is %d.' % (digit(n)))
print('Tens place is %d.' % (tens(n)))
print('Hundreds place is %d.' % (hundreds(n)))
print('Thousands place is %d.' % (thousands(n)))
print('Sum of all digits is %d.' % sum_digits(n))
            
