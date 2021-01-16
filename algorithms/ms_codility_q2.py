def solution_2(blocks):
    """
    maximum steps
    :param blocks:
    :return:
    """
    n = len(blocks)
    i = 0
    distances = []
    if n <= 1:
        return 0
    # [2,3,4,7,6,8,5]


def solution(blocks):
    """
    - Algorithms/ Steps followed to solve this problem
    1) Distance calculated by K - J+1 (J<=K)
    2) Can only jump adjacent block, second block greater or equal next block
    3) Using brute force approach
    4) Iterate to get the distances that a frog can jump for each index
    5) Return maximum value
    6) Time Complexity O(n*n)
    6) Space Complexity O(n)
    :return:
    """
    # Stores the forward steps that can be made by a frog
    forward_steps = 0
    # Stores backward moves that can be made
    backward_steps = 0

    # Iterate through to get maximum gap among the blocks in which the frog can jump
    for position, block in enumerate(blocks):
        # keep track of the current position
        current_position = position
        # Compute forward steps that can be made from the current position
        while len(blocks) - 1 != position and blocks[position] <= blocks[position + 1]:
            forward_steps += 1
            position += 1

        position = current_position
        # Compute backward steps that can be made from the current position
        while position - 1 != -1 and blocks[position] <= blocks[position - 1]:
            forward_steps += 1
            position -= 1

        forward_steps += 1
        if forward_steps > backward_steps:
            backward_steps = forward_steps
            forward_steps = 0
        else:
            forward_steps = 0

    return backward_steps


if __name__ == "__main__":
    print(solution())
