# A program to display fibonacci sequence
def fibonacci(n, result):
    if n in result:
        return result[n]
    res =  fibonacci(n-1, result) + fibonacci(n-2, result)
    result[n] = res
    return result[n]


terms  = 10

print("Print Fibonacci numbers: ->")

for i in range(terms):
    print(fibonnaci(i, {0: 0, 1:1}))