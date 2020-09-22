PI = 3.1415926

# 기본 함수 생성

def circleArea(radius):
    print("반지름이",radius,"인 원의 면적:", PI*radius**2)

def circleCircumference(radius):
    print("반지름이",radius,"인 원의 둘레:",2*PI*radius)

radius=int(input("반지름의 값을 입력하세요:"))
circleArea(radius)
circleCircumference(radius)


# "함수" 개념

def circleArea(radius):
    return PI*radius**2

def circleCircumference(radius):
    return 2*PI*radius

radius=int(input("반지름의 값을 입력하세요:"))
print("반지름이",radius,"인 원의 면적:", circleArea(radius))
print("반지름이",radius,"인 원의 둘레:",circleCircumference(radius))


# global

def circleArea(radius):
    global area
    area = PI*radius**2

def circleCircumference(radius):
    global circimference
    circimference = 2*PI*radius

radius=int(input("반지름의 값을 입력하세요:"))
area = 0 
circimference = 0
circleArea(radius)
circleCircumference(radius)
print("반지름이",radius,"인 원의 면적:", area)
print("반지름이",radius,"인 원의 둘레:", circimference)
