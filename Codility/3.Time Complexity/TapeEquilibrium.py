import math
def solution_v1(A):
    sum_list = sum(A)
    sum_diff = []
    for i in range(1, len(A)):
        sum_sub = sum(A[ :i])
        sum_diff.append(abs(2 * sum_sub - sum_list))
    return min(sum_diff)


def solution(A):
    if len(A) == 2:
        return abs(A[0] - A[1])
    else:
        sum_list = sum(A)
        sum_sub = 0
        min_diff = math.inf
        for num in A[:-1]:
            sum_sub += num
            diff = abs(2 * sum_sub - sum_list)
            if diff == 0:
                return 0
            elif diff < min_diff:
                min_diff = diff
        return min_diff
            
print(solution([3,1,2,4,3]))