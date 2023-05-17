def climbStairs(n: int) -> int:
    one, two = 1, 1
    for _ in range(n - 1):
        print("one", one)
        print("two", two)
        temp = one
        one = one + two
        two = temp
    return one


print(climbStairs(5))