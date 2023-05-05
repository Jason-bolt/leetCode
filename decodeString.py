"""
Author: Jason Kwame Appiatu
Latest Update Date: 3rd, March, 2023
"""

from ast import List

def decodeString(s: str) -> str:
    if s.find('[') != -1:
        vars: object = {}
        num: int
        num_temp: List[int] = []
        first_bracket: int
        second_bracket: int
        content: str = ''
        bracket_check: List[int] = []

        num = int(s[s.find('[')-1])
        first_bracket = s.find("[")
        
        if (first_bracket >= 3):
            end = first_bracket - 4
        else:
            end = -1

        for i in range(first_bracket - 1, end, -1):
            if s[i].isdigit():
                num_temp.insert(0, s[i])
            else:
                break
        # num = int(s[int(''.join(num_temp))])
        # print(''.join(num_temp))
        num = int(''.join(num_temp))
        # print(num_temp)
        # print(num)
                

        bracket_check.append(s[first_bracket])

        for i in range(first_bracket + 1, len(s)):
            if s[i] == '[':
                bracket_check.append(s[first_bracket])
            if s[i] == ']' and len(bracket_check) == 1:
                second_bracket = i
                break
            elif s[i] == ']' and len(bracket_check) > 1:
                bracket_check.pop()
            content+=s[i]

        # print(second_bracket, "sencond")
        # print(first_bracket, "first")
        # print(len(s) - 1, "last")
        
        if (first_bracket == 1 and second_bracket == len(s)-1):
            # print(num * content)
            return decodeString(num * content)
        elif (first_bracket == 1 and second_bracket < len(s)-1):
            # print((num * content) + s[second_bracket + 1:])
            return decodeString((num * content) + s[second_bracket + 1:])
        elif (first_bracket > 1 and second_bracket < len(s)-1):
            # print(s[0:first_bracket - 1] + (num * content) + s[second_bracket + 1:])
            return decodeString(s[0:first_bracket - len(str(num))] + (num * content) + s[second_bracket + 1:])
        elif (first_bracket > 1 and second_bracket == len(s)-1):
            # print(s[0:first_bracket - 1] + (num * content) + s[second_bracket + 1:])
            return decodeString(s[0:first_bracket - len(str(num))] + (num * content))
    elif s.isdigit():
        return ""
    else:
        return s



# TEST CASES

# test_string = "300[a]"
# test_string = "300[2[a]]"
# test_string = "3[a]2[bc]"
# test_string = "3[a2[c]]4[cds]dvf"
# test_string = "2[abc]3[cd]ef"
test_string = "2[abc]3[3[cd]2[a2[cd]]]ef"

print (decodeString(test_string))