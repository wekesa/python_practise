def solution_2(ranks):
    """
    :param ranks:
    :return: integer n
    - Algorithms/ Steps followed to solve this problem
    - A soldier has to report to a rank higher by 1
    - Iterate to get a list of soldiers reporting to some higher rank soldier
    - By use of list comprehensions
    - Return the length of the list
    """
    # Return 0 if the array is empty
    if len(ranks) == 0:
        return 0
    return len([i for i in ranks if i + 1 in ranks])


if __name__ == "__main__":
    print(solution_2([3,4,3,2,3,0]))


