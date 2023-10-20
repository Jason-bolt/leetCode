def titleToNumber(columnTitle: str) -> int:
    count  = len(columnTitle)
    firstCharacter = "A"
    letters = {}

    for i in range(26):
        letters[chr(ord(firstCharacter) + i)] = i + 1
        
    ans = 0
    power = count - 1
    for i in range(count):
        ans += letters[columnTitle[i]] * (26 ** (power))
        print("letter", columnTitle[i], "ans", ans)
        power = power - 1
        
        
    
    
titleToNumber("ZY")