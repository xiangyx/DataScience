def solution_v1(A):
    max_num = max(A)
    if max_num <= 0:
        return 1
    else:
        set_perm = {i for i in range(1, max_num + 1)}
        set_A = set(A)
        set_diff = set_perm.difference(set_A)
        if len(set_diff) == 0:
            return max_num + 1
        else:
            return min(set_diff)

def solution(A):
    set_A = set(A)
    for num in range(1, len(set_A) + 1):
        if num not in set_A:
            return num
    return len(set_A) + 1

print(solution([-1,-10,-3, 1]))



            

