x = int(input())
y = int(input())
print((x+y)//2)
print((x-y)//2)

# 첫번째 수를 a라 하자. 
# x = a + a - y -> x = 2a - y -> a = (x+y) / 2
# 두번째 수를 b라 하자. 
# x = b + y + b -> x = 2b + y -> b = (x-y) / 2
