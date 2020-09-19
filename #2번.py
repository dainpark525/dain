#2번

a=int(input("홀수인 정수를 입력 하세요."))

for b in range(1,a+1,2):
  c=(a-b)//2
  print(" "*c,"*"*b)

for b in range(a,0,-2):
  c=(a-b)//2
  print(" "*c,"*"*b)
