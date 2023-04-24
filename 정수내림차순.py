def solution(n):
    ls=list(str(n))
    ls.sort(reverse=True)
    res=int("".join(ls))
    return res
