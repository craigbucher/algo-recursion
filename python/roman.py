def roman_num(num):
    BASE_CASES = {"": 0, "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

    if num in BASE_CASES:
        return BASE_CASES[num]

    first, second = map(roman_num, num[:2])
    if first < second:
        return second - first + roman_num(num[2:])
    else:
        return first + roman_num(num[1:])


print(roman_num('XXX'))