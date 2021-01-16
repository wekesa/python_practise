# Codility code examples
from collections import deque


def rotate_array_values(A, K):
    for i in range(1, K + 1):
        # start, end = 0, len(A)-1
        # end_value = A[end]
        # new_array = [end_value]
        # for i in range(start, end):
        #     new_array.append(A[i])
        A.append(A.pop(0))

    return A


# A function to get odd occurrence of an integer given a list of integers
def get_odd_occurrence(array):
    array_size = len(array)
    for i in range(0, array_size):
        count = 0
        for j in range(0, array_size):
            if array[i] == array[j]:
                count += 1
        if count % 2 != 0:
            return array[i]
    return -1


# Optimized solution for odd occurrences

def get_odd_optimized(array):
    # initialize results
    result = 0

    for ele in array:
        # XOR with the result
        result = result ^ ele
    return result


def rotate_list_using_deque(A):
    items = deque([1, 2, 3, 4, 5])
    items.rotate(1)
    return items


def min_jumps(X, Y, D):
    d = Y - X
    jumps = int(d / D)
    rem = d % D
    if rem != 0:
        jumps += 1
    return jumps


def find_missing_value(a):
    x1 = a[0]
    n = len(a)
    x2 = 1

    for i in range(1, n):
        x1 = x1 ^ a[i]

    for i in range(2, n + 2):
        x2 = x2 ^ i

    return x1 ^ x2


def permutation_solution(A):
    s = sum(A)
    m = float('inf')
    left_sum = 0
    for i in A[:-1]:
        left_sum += i
        m = min(abs(s - 2 * left_sum), m)
    return m


def earliest_jump_time(A, X):
    for index, value in enumerate(A):
        if value == X:
            return index
    return -1


def max_counter(A, N):
    B = [0] * N
    baseValue = 0;
    maxCount = 0;
    for x in A:
        if 1 <= x <= N:
            B[x - 1] = max(B[x - 1], baseValue) + 1
            maxCount = max(B[x - 1], maxCount)
        else:
            baseValue = maxCount

    for i in range(N):
        B[i] = max(B[i], baseValue)

    return B;


def reversed_string_func(s):
    list_string = []
    index = len(s)
    while index > 0:
        list_string += s[index-1]
        index -= 1
    return ''.join(list_string)


def missing_integer_solution(A):
    """
        Algorithm:
         - Identify the maximum and minimum values
         - If max is less than zero return 1
         - If length == 1
         - create a temporary list to keep order of values expected
         - Else loop through the array to find a missing values
         - return the value
         This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
        """
    maximum_value = max(A)
    if maximum_value < 1:
        return 1

    if len(A) == 1:
        return 2 if A[0] == 1 else 1

    # Create a list with initial values of zero
    tracking_list = [0] * maximum_value

    for i in range(len(A)):
        if A[i] > 0:
            if tracking_list[A[i] - 1] != 1:
                tracking_list[A[i] - 1] = 1

    for i in range(len(tracking_list)):
        if tracking_list[i] == 0:
            return i + 1
    return i + 2


def countdiv_solution(A, B, K):
    # Add 1 explicitly as A is divisible by M
    if (A % K == 0):
        return (int(B / K) - int(A / K)) + 1

    # A is not divisible by M
    return (int(B / K) - int(A / K))


def equilibrium(A):
    """
    Algorithm
     -
    :param A:
    :return:
    """
    size = len(A)
    right_sum, left_sum = 0, 0

    # Computing right_sum
    for i in range(1, size):
        right_sum += A[i]

    i, j = 0, 1

    # Checking the point of partition
    # i.e. left_Sum == right_sum
    while j < size:
        right_sum -= A[j]
        left_sum += A[i]

        if left_sum == right_sum:
            return A[i + 1]
        j += 1
        i += 1

    return -1


def balance_brackets(S):
    stack = []

    # Traversing the Expression
    for char in S:
        if char in ["(", "{", "["]:

            # Push the element in the stack
            stack.append(char)
        else:

            # IF current character is not opening
            # bracket, then it must be closing.
            # So stack cannot be empty at this point.
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False

    # Check Empty Stack
    if stack:
        return False
    return True


def genomic_sequence(S, P, Q):
    """
    :param S:
    :param P:
    :param Q:
    :return:
    - ACGT represent 1,2,3, 4
    - String that contains only these characters
    -
    """
    n = len(S)
    sumA = [0] * (n + 1)
    sumC = [0] * (n + 1)
    sumG = [0] * (n + 1)
    sumT = [0] * (n + 1)
    for idx, nucleotide in enumerate(S):
        sumA[idx + 1] = sumA[idx]
        sumC[idx + 1] = sumC[idx]
        sumT[idx + 1] = sumT[idx]
        sumG[idx + 1] = sumG[idx]
        if nucleotide == 'A':
            sumA[idx + 1] += 1
        elif nucleotide == 'C':
            sumC[idx + 1] += 1
        elif nucleotide == 'G':
            sumG[idx + 1] += 1
        else:
            sumT[idx + 1] += 1
    result = [0] * len(P)
    for i in range(len(P)):
        AsInRange = sumA[Q[i] + 1] - sumA[P[i]]
        CsInRange = sumC[Q[i] + 1] - sumC[P[i]]
        GsInRange = sumG[Q[i] + 1] - sumG[P[i]]
        # TsInRange = sumT[Q[i] + 1]- sumT[P[i]]
        if AsInRange > 0:
            result[i] = 1
        elif CsInRange > 0:
            result[i] = 2
        elif GsInRange > 0:
            result[i] = 3
        else:
            result[i] = 4
    return result

list_a = [1, 2, 3, 5]
# print(rotate_array_values(list_a, 3))
# print(rotate_list_using_deque(list_a))
# arr = [2, 3, 5, 4, 5, 2, 4, 3, 5, 2, 5, 4, 2 ]
# print(get_odd_occurrence(arr))
# print(get_odd_optimized(arr))
# print(min_jumps(10, 85, 40))
# print(find_missing_value(list_a))
# print(earliest_jump_time([1, 3, 1, 4, 2, 3, 5, 4], 5))
# print(max_counter(list_a, 5))
# print(missing_integer_solution([1, 3, 6, 4, 1, 2]))
# print(permutation_check([1,2,3,4,5,7,6]))
# print(countdiv_solution(11, 345, 17))
print(reversed_string_func("abc"))