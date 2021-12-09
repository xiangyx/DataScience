def solution_v1(A, X):
    if X not in A:
        return -1
    elif len(set(A)) > 1:
        set_position = set()
        for index, value in enumerate(A):
            if value not in set_position and value <= X:
                set_position.add(value)
            if len(set_position) == X:
                return index
    else:
         return -1


def solution(A, X):
    set_position = {i for i in range(1, X + 1)}
    for index, value in enumerate(A):
        if value in set_position:
            set_position.remove(value)
        if len(set_position) == 0:
            return index
    return -1

print(solution([1,3,1,4,2,3,5,4], 5))
