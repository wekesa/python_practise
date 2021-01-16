"""
- Dynamic programming is an approach of solving a programming challenge by
breaking it down into sub-problems and save the result for future so that we
do not have to recompute the problem again
- Two methods here
    - Top down
    - Bottom up
"""






"""
- Iterator Implementation
"""
class PowTwo:
    """
    Class to implement an iterator of powers of two
    """
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 **self.n
            return result
        else:
            raise "Stop iteration"

numbers = PowTwo(3)
