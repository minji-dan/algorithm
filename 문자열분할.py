#20221028 cj

def solution(s, n):

    cnt = 0 #분할횟수
    res=[[0] for i in range(n+1)]
    alpha="abcdefghijklmnopqrstuvwxyz"

    value=len(s)//3
    print(value)
    tmp=0

    #분할 
    for i in range(n+1):
        res[i]=s[tmp:tmp+value]
        tmp=tmp+value


    cnt=[[0] for i in range(n+1)]
    #알파벳 횟수

    for i in range(n+1):
        str=res[i] #res[0]="aab"
        print(str)
        alpha_cnt=[0 for i in range(len(alpha))]
        for j in range(len(str)): #문자열 마다 
            for w in range(len(alpha)): #알파벳 확인 
                if(str[j]==alpha[w]):
                    alpha_cnt[w]=alpha_cnt[w]+1
        cnt[i]=max(alpha_cnt)
        print("가장 큰 값", cnt[i])

    return cnt[i]
