# Tower of Hanoi is a mathematical puzzle where we have three rods and n disks.
# The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
# 1) Only one disk can be moved at a time.
# 2) Each move consists of taking the upper disk from one of the stacks and placing it on top of
#    another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
# 3) No disk may be placed on top of a smaller disk.


def tower_of_hanoi(n, source, destination, auxilliary):
    if n == 1:
        print("Move disk 1 from source ", source, " to destination ", destination)
        return
    tower_of_hanoi(n-1, source, auxilliary, destination)
    print("Move disk ", n, "from source ", source, " to destination ", destination)
    tower_of_hanoi(n-1, auxilliary, destination, source)


# Test code for our function

if __name__ == '__main__':
    n = 3
    tower_of_hanoi(n, 'S', 'D', 'A')


""" first iteration  
3 S D A

2 S A D

1 S D A

0 S A D

"""