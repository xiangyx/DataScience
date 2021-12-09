def solution_v1(A):
    length = len(A)
    missing_value = [i for i in range(1, length+2) if i not in A]
    return missing_value[0]

def solution_v2(A):
    complete_list = list(range(1, len(A) + 2))
    for num in A:
        complete_list.remove(num)
    return complete_list[0]

def solution(A):
    set_all = set(list(range(1, len(A) + 2)))
    set_A = set(A)
    (missing_value, ) = set_all.difference(set_A)
    return missing_value

print(solution([2, 3, 1, 5]))
