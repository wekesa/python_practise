def solution(ranks):
    """
    - Algorithms/ Steps followed to solve this problem
    1) Get the
    2)
    3)
    4)
    5)
    6) Time Complexity O()
    6) Space Complexity O()
    :return:
    """
    map_of_ranks = {}
    reporting_soldiers = 0

    for rank in ranks:
        if map_of_ranks.get(rank):
            map_of_ranks[rank] = map_of_ranks[rank] + 1
        else:
            map_of_ranks[rank] = 1

    for rank in map_of_ranks:
        higher_rank = rank + 1
        if map_of_ranks.get(higher_rank):
            reporting_soldiers += map_of_ranks[rank]
    return reporting_soldiers


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
    print(solution([3,4,3,2,3,0]))
    print(solution_2([3,4,3,2,3,0]))