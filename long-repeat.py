def long_repeat(line):
    """
        length the longest substring that consists of the same char
    """
    # your code here
    if len(line) == 0:
        return 0
    else:
        l = [i for i in line]
        l_1 = set(l)
        result = {}
        for i in l_1:
            result[i] = 1
            for j in range(len(l)-1):
                if l[j] == i and l[j+1] == i:
                    result[i] += 1
        return max(result.values())

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')