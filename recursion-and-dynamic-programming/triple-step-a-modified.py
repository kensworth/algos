#A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs


def countStairs(num):
    if num < 0:
        return 0
    elif num == 0:
        return 1
    return countStairs(num - 2) + countStairs(num - 1) + countStairs(num - 3)
    
print(countStairs(5))
