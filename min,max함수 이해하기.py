slist=[]
for num in range(1,11,1):
    num2=int(input(str(num)+"번째 숫자를 입력하시오>>"))
    slist.append(num2)


print("입력된 값은",slist,"이고")

max_num=slist[0]
min_num=slist[0]

for num2 in range(1,10,1):
    if max_num<slist[num2]:
        max_num=slist[num2]

    if min_num>slist[num2]:
        min_num=slist[num2]

print("가장 큰 값은",max_num,"이고")
print("가장 작은 값은",min_num,"입니다.")