def checkio(words: str) -> bool:
    ele = words.split()
    count = 0
    if len(ele) < 3:
        return False
    else:
        for index in range(len(ele)-2):
            if all([ele[index].isalpha(),ele[index+1].isalpha(),ele[index+2].isalpha()]):
                count += 1
    if count > 0:
        return True
    else:
        return  False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("Hello World hello") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("Hi") == False, "Hi"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")