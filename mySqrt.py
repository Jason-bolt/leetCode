def mySqrt(x: int) -> int:
    if x <= 1:
        return x
    num: int = 2
    print(x)
    while True:
        print(num)
        check: int = ((num * num) > x)
        if check:
            return num - 1
        num += 1

print (mySqrt(5))