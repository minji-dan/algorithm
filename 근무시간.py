import sys

def cal(num1, num2):
    num1=num1.split(":")
    num2=num2.split(":")

    num1=list(map(int, num1))
    num2=list(map(int, num2))
    
    num1=num1[0]*60+num1[1]
    num2=num2[0]*60+num2[1]
    
    return num2-num1



result=0
for i in range(5):
    num1, num2=input().split()
    result=result+cal(num1, num2)

print(result)
