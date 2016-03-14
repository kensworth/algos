#A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time. Implement a method to count how many possible ways the child can run up the stairs
count = {'count': 0}
def countStairs(num):
    if num < 0:
        return
    elif num == 0:
        count['count'] += 1
    countStairs(num - 1)
    countStairs(num - 2)
    countStairs(num - 3)

countStairs(15)
print(count['count'])
