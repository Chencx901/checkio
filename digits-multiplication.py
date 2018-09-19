def checkio(number: int) -> int:
    p = 1
    while number // 10 != 0:
        if number % 10 !=0: p *= (number%10)
        number = number //10 
    p = p*number
    return p

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")