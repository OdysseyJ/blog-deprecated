n = int(input())

#  if n <= 9:
#      print(1*n)
#  if n >= 10 and n <= 99:
#      print((1*9)+(2*(n-9)))
#  if n >= 100 and n <= 999:
#      print((1*9)+(2*90)+(3*(n-99)))
#  if n >= 1000 and n <= 9999:
#      print((1*9)+(2*90)+(3*900)+(4*(n-999)))

length = len(str(n))
sum_ = 0
for i in range(1, length+1):
    if i == length:
        sum_ += i*(n-int('9'*(i-1) if i>1 else 0))
    else:
        sum_ += i*int('9'+'0'*(i-1))

print(sum_)
