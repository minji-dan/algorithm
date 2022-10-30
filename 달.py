#20221030 롯정코테

def solution(p):
    length=len(p)

    if(length==1):
        return -1
    for i in range (1,length):
        if (p[i-1]<p[i]):
            flag=1 # 오름차순
        else:
            flag=0 # 내림차순 

    if flag==1 and p[i]!=15:
        return 1
    elif flag==1 and p[i]==15:
        return 0
    elif flag==0 and p[i]!=0:
        return 0
    elif flag==0 and p[i]==0:
        return 1
