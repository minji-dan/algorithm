def solution(n):
    if n < 3:
        return -1

    answer=0
    tmp = n % 5 

    #3의 배수 아니면 (12, 106 같은 경우 )
    if tmp %3 != 0 and tmp + 5 > n:
        return -1

    if tmp % 3 !=0: 
        box3 = n%5 
        box5 = n - box3 
        while (n-box5-box3)>=0:
            box5 = box5 - 5 
            box3 = box3 + 5 
            if box3 % 3 == 0 or box3 ==0 or box5 ==0:
                break
        answer=box3/3 + box5/5
        if answer%1 != 0:
            return -1

    elif tmp % 3 ==0: 
        box3=tmp/3
        #box5에 들어갈 개수 
        box5 = (n - tmp) / 5 
        if box5 % 1 != 0:
            return -1
        answer=box3+box5
    else:
        return -1
    return answer
