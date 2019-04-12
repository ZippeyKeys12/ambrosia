from typing import Callable


def time(func: Callable, *args):
    import time
    start = time.time()
    print(func(*args))
    end = time.time()
    print("Elapsed Time: {}".format(end-start))


def multiple_sum(num: int) -> int:
    total = 0
    for x in range(num + 1):
        if x % 3 == 0 or x % 5 == 0:
            total += x
    return total


def even_fibonacci(num: int):
    if num < 0 or type(num) != int:
        raise ValueError("Need positive integer")

    if num <= 2:
        return 0

    last = 1
    curr = 2
    total = 2

    while(curr < num):
        temp = curr
        curr += last
        last = temp

        if curr % 2 == 0:
            total += curr

    return total


def largest_prime_factor(num: int) -> int:
    biggest = 0

    i = 2
    while i**2 <= num:
        if num % i == 0:
            num //= i
            biggest = i
        else:
            i += 1

    if num > biggest:
        biggest = num

    return biggest


def largest_palindrome_product(digits: int) -> int:
    if digits <= 0:
        raise ValueError("Digits must be greater than 0")

    top = int('9'*digits)

    max_palin = 0
    for i in range(top, 0, -1):
        for j in range(top, 0, -1):
            num = i*j
            text = str(num)

            if num > max_palin and text == text[::-1]:
                max_palin = num

    return max_palin


def largest_palindrome_product2(digits: int) -> int:
    if digits <= 0:
        raise ValueError("Digits must be greater than 0")

    i = j = int('9'*digits)

    max_palin = 9
    while j != 0:
        num = i*j

        if num <= max_palin:
            j -= 1
            i = j

            if i*j <= max_palin:
                return max_palin

            continue

        text = str(num)
        if text == text[::-1]:
            max_palin = num

        i -= 1

    return max_palin


def test():
    time(multiple_sum, 1000)
    time(even_fibonacci, 4_000_000)
    time(largest_prime_factor, 600_851_475_143)
    time(largest_palindrome_product, 3)
    time(largest_palindrome_product2, 3)
