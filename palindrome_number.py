n =int(input("enter a number:  "))
inverse =0
m=n
while n != 0:
    inverse = ( inverse * 10 ) + ( n % 10 )
    n = n // 10 
if m ==inverse:
    print("the number is palindrome")
else:
    print("the number is not")
