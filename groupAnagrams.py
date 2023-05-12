from ast import List

def groupAnagrams(strs: List) -> List:

    # Keep first word
    # Group all anagrams of that work while popping 
    # them from the array
    # When you reach the end, append that array to a 
    # larger array
    # Return larger array

    if len(strs) > 100 or len(strs) < 0:
        return
    strs = list(set(strs))

    output = []
    anagrams = []
    length = len(strs) - 1
    while len(strs) > 0:
        testWord = strs[0]
        anagrams.append(strs.pop(0))

        pos = 0
        while (len(strs) > 0 and pos < len(strs)):
            if sorted(testWord) == sorted(strs[pos]):
                anagrams.append(strs[pos])
                strs.remove(strs[pos])
                continue
            pos = pos + 1
        if len(strs) > 0:
            if sorted(testWord) == sorted(strs[-1]):
                anagrams.append(strs[-1])
                strs.remove(strs[-1])
        output.append(anagrams)
        anagrams = []
    return output


            

# print(groupAnagrams(["hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"]))
# print(groupAnagrams(["w","w","w","w"]))
# print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
# print(groupAnagrams(["eat","tea","tan","ate","nat","bat","hhhhu","tttti","tttit","hhhuh","hhuhh","tittt","eat","tea","tan","ate","nat","bat","hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"]))


# ls = ['hay', 'vdfv']
# for (i, n) in enumerate(ls):
#     print(i)
#     print(n)

# print(list(set(["eat","tea","tan","ate","nat","bat","nat"])))

def groupAnagramsOptimized(strs: List) -> List:
    result = {}
    for word in strs:
        sorted_word = ''.join(sorted(word))
        print(sorted_word)
        if sorted_word not in result:
            result[sorted_word] = [word]
        else:
            result[sorted_word].append(word)
    return result.values()


print(groupAnagramsOptimized(["hhhhu","tttti","tttit","hhhuh","hhuhh","tittt"]))

