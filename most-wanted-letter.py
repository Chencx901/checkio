import re
def checkio(text: str) -> str:

    newtext = text.lower()
    result = {}
    for i in newtext:
        if re.match("[a-z]", i):
            if result.get(i) == None:
                result[i] = 1
            else:
                result[i]+= 1
    max_value = max(set(result.values()))
    return sorted([key for key,value in result.items() if value == max_value])[0]

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")