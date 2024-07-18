def walkRecursion(steps):
    if steps == 0:
        return 
    walkRecursion(steps - 1)
    print(f"You take the steps: {steps}")

walkRecursion(100)

"""
I can solve a lot problems either iterably or recursibly, they're kinda similar. 
However, in certain situations is better depending the situation, recursion is more useful in DS and
algorithims.

"""


#ITERATION 
def factorial(x):
    result = 1
    if x > 0:
        for i in range(1, x + 1):
            result *= i
    return result

print(factorial(10))


#RECURSION
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)
    


# recursion = a function that calls itself from within
#                      helps to visualize a complex problem into basic steps
#                      problems can be solved more easily iteratively or recursively
#                      iterative = faster, complex
#                      recursive = slower, simpler