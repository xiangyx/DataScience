def solution_v1(A):
    perm = list(range(1, len(A) + 1))
    for num in A:
        if num in perm:
            perm.remove(num)
        if len(perm) == 0:
            return 1
    return 0


def solution(A):
    perm = list(range(1, len(A) + 1))
    if sorted(A) == perm:
        return 1
    else:
        return 0
        
print(solution([4,3,1]))