# 다음과 같이 import를 사용할 수 있습니다.
# import math

def solution(garden):
    # 여기에 코드를 작성해주세요.
    answer = 0
    length=len(garden)
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    
    res = [[0]*length for _ in range(length)]
    #print(res)
    
    # 1 좌표 찾기
    def findValue(garden):
        for x in range(length):
            for y in range(length):
                if garden[x][y] == 1:
                    #print("실행",x, garden)
                    #상하좌우 값 바꾸기 
                    res[x][y]=1
                    for i in range(4):
                        nx=x+dx[i]
                        ny=y+dy[i]
                        if 0<=nx<length and 0<=ny<length:
                            res[nx][ny]=1
        for x in range(length):
            for y in range(length):
                garden[x][y] = res[x][y]
    
    #0 값 남아있는지 확인 
    def exec(garden):
        for x in range(length):
            for y in range(length):
                if garden[x][y] == 0:
                    return True
        return False
        
    cnt = 0
    while(exec(garden)):
        cnt = cnt + 1
        findValue(garden)
        #print('실행후', garden)

    
    return cnt 
    

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(garden1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

garden2 = [[1, 1], [1, 1]]
ret2 = solution(garden2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

garden3 = [[0, 1, 0], [0,1,0],[0,0, 0]]
ret3 = solution(garden3)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret3, "입니다.")
