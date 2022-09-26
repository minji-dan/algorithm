# 2019 KAKAO BLIND RECRUITMENT
# 실패율

# 채점 결과
# 정확성: 88.9
# 합계: 88.9 / 100.0

# 전체 스테이지의 개수 N
# 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 stages

def solution(N, stages):
    answer = []
    # 1. 스테이지 개수만큼 배열생성
    length=len(stages)
    cnt = [_ for _ in range(1,N+1)]
    print(cnt, "cnt: stage 개수")
    
    # 2. 각 스테이지 도전자
    chal = [0 for _ in range(N)]
    for i in range(length):
        for j in range(N):
            if stages[i] >= cnt[j]:
                chal[j] = chal[j]+1
    print(chal, "chal: stage별 도전자")
    
    # 3. 도전 중인 스테이지 번호 
    curr = [0 for _ in range(N+1)]
    for i in range(length):
        # 마지막 스테이지라면
        if stages[i] == N+1:
            curr[N]=curr[N]+1
        else:
            for j in range(N):
                if stages[i] == cnt[j]:
                    curr[j] = curr[j]+1
    print(curr, "curr: 도전 중인 스테이지")
    
    #실패율: 도전 중인 스테이지 / stage별 도전자
    cal = [0 for _ in range(N)]
    tmp = [0 for _ in range(N)]
    for i in range(N):
        # 이 처리를 해줬어야 했다: 도전자가 0인 경우 0으로 나눌 수 없습니다.
        if chal[i]==0:
            cal[i]=0
            tmp[i]=cal[i]
            continue
        cal[i] = curr[i] / chal[i]
        tmp[i]=cal[i]
    print(cal, "실패율: cal=curr/chal")
    
    #실패율 내림차순 정렬 
    tmp.sort(reverse=True)
    print(tmp, "tmp, 실패율 내림차순 정렬")
    
    #스테이지 번호 
    num = [0 for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if tmp[i]==cal[j]:
                num[i]=j+1
                cal[j]=-1
                break
    print(num)
    
    return num
