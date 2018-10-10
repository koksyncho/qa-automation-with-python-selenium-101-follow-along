import math

def sum_of_digits(n):
    digitSum = 0;
    if n < 0:
        n = n * (-1)
    while n:
        digitSum += n % 10
        n = n // 10
    return digitSum

def to_digits(n):
    digitList = []
    while n:
        digitList.append(n % 10)
        n = n // 10
    return list(reversed(digitList))

def to_number(digits):
    number = 0
    multiplier = 1
    for i in reversed(digits):
        number += i * multiplier
        multiplier *= 10
    return number

def count_vowels(str):
    vowels = list("aeiouyAEIOUY")
    vowelCount = 0
    vowelCount = sum(str.count(c) for c in vowels)
    return vowelCount

def count_consonants(str):
    consonants = list("bcdfghjklmnpqrstvxzBCDFGHJKLMNPQRSTVXZ")
    consonantCount = 0
    consonantCount = sum(str.count(c) for c in consonants)
    return consonantCount

def prime_number(number):
    if number % 2 == 0 and number > 2:
        return False
    return all(number % i for i in range(3, int(math.sqrt(number)) + 1, 2))

def fact_digits(n):
    sum = 0
    while n:
        currentDigit = n % 10
        factorialOfDigit = 1
        while currentDigit:
            factorialOfDigit *= currentDigit
            currentDigit -= 1
        sum += factorialOfDigit
        n = n // 10
    return sum

def fibonacci(n):
    fibList = []
    if n > 2:
        fibList = [1, 1]
        for i in range(2, n):
            fibList.append(fibList[i-1] + fibList[i-2])
    else:
        if n == 2:
            fibList = [1, 1]
        if n == 1:
            fibList = [1]
    return fibList

def fib_number(n):
    fibNumber = ''.join(str(elem) for elem in fibonacci(n))
    return int(fibNumber)

def palindrome(n):
    input = str(n)
    reverseInput = reversed(input)
    if list(input) == list(reverseInput):
        return True
    else:
        return False

def char_histogram(string):
    dict = {}
    for c in string:
        if c in dict.keys():
            dict[c] += 1
        else:
            dict[c] = 1
    return dict

if __name__ == "__main__":
    print(sum_of_digits(914))
    print(to_digits(123))
    print(to_number([3,2,1]))
    print(count_vowels("AOFKQOJpasidoiqpe"))
    print(count_consonants("Hello this is a test sentence"))
    print(prime_number(11))
    print(fact_digits(9))
    print(fibonacci(9))
    print(fib_number(9))
    print(palindrome("abba"))
    print(char_histogram("asdhoqodah"))
