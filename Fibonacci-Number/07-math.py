def solve(n):
    # CODE HERE
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return solve(n - 1) + solve(n - 2)
"""
Program Explanation:

def solve(n):
This line defines a function called solve() that takes in a single parameter n.

    if n == 0:
        return 0
This line checks if the value of n is equal to 0. If it is, the function returns 0.

    elif n == 1:
        return 1
This line checks if the value of n is equal to 1. If it is, the function returns 1.
    else:
        return solve(n - 1) + solve(n - 2)
If the value of n is not 0 or 1, the function calls itself with n - 1 and n - 2 as arguments, and returns the sum of the two recursive calls.

This is an example of a recursive function, as it calls itself with a modified version of the original input. In this case, the function keeps calling itself with smaller and smaller values of n until it reaches the base case (n equal to 0 or 1), at which point it returns a value and the recursive calls can start to unwind.

"""
