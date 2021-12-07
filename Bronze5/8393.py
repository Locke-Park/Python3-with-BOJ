#가우스 덧셈법을 이용한 풀이

a = int(input())

print(int(a * (a+1) / 2))

#반복문과 리턴함수를 이용한 풀이

n = int(input())

def x(n):
  total = 0 
  for i in range(1, n+1):
    total = total + i
  return total

print(x(n))


