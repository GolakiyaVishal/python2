"""Compute number of distinct values in an array."""

def solution(A):
    dSet = set()

    for e in A:
        dSet.add(e)

    return len(dSet)


if __name__ == '__main__':
    print(solution([0,1,2,5,0,2,1,5,2,1,0,5]))