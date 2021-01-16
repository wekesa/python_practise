def solution(S):
    """
    - Algorithms/ Steps followed to solve this problem
    1) Given a string S
    2) Split left to right approach
    - Time Complexity O(n)
    - Space Complexity O(1)
    :return:
    """
    to_delete = 0
    i = 0
    n = len(S)
    count_a = 0
    count_b = 0

    if n == 0:
        return 0
    while i < n:
        if S[i] == 'A':
            count_a += 1
            if count_b > to_delete:
                to_delete += 1
        else:
            count_b += 1
        i += 1
    return min([count_a, count_b, to_delete])


if __name__ == "__main__":
    print(solution('BBABAA'))
