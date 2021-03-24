def number_to_word(n):
    """Assumes is an integer from 1 - 1000.
    Returns number in words ex: 122 --> one hundred and twenty-two."""
    # num_to_alpha contains the unique values for numbers that will be returned according to repetitive patterns
    num_to_alpha =\
        {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
         11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen',
         18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
         70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'one hundred', 1000: 'one thousand'}
    # Numbers below 21 , 100, 1000 are unique words (cannot be formed using a repetitive rule)
    if 0 < n < 21 or n == 100 or n == 1000:
        return num_to_alpha[n]
    mod = n % 10
    # Numbers in range (21 - 99) have a single rule except the multiples of 10 (formed by a single word)
    if 20 < n < 100:
        if n % 10 != 0:
            return f'{num_to_alpha[n // 10 * 10]}-{num_to_alpha[mod]}'
        return num_to_alpha[n]
    # Numbers above 100 have a single rule except the following:
    if 100 < n < 1000:
        # a) multiples of 100
        if n % 100 == 0:
            return f'{num_to_alpha[n // 100]} hundred'
        # b) numbers whose last 2 digits are above 20 and are also multiples of 10
        if not n % 100 == 0 and n % 100 > 20 and n % 10 == 0:
            return f'{num_to_alpha[n // 100]} hundred and {num_to_alpha[n % 100]}'
        # c) numbers whose last 2 digits are below 20 and not multiples of 10
        if n % 100 < 21:
            second_part = num_to_alpha[n % 100]
            return f'{num_to_alpha[n // 100]} hundred and {second_part}'
        # d) numbers whose last 2 digits are above 20 and not multiples of 10
        if n % 100 > 20:
            return f'{num_to_alpha[n // 100]} hundred and {num_to_alpha[((n % 100) // 10) * 10]}-' \
                f'{num_to_alpha[(n % 100) % 10]}'
    # To prevent counting False values
    if n <= 0 or n > 1000:
        return ''


def count():
    """Cleans numbers from spaces and hyphens and returns count."""
    all_numbers = [number_to_word(x) for x in range(1, 1001)]
    numbers_without_spaces = [number.replace(' ', '') for number in all_numbers]
    clean_numbers = [number.replace('-', '') for number in numbers_without_spaces]
    total = 0
    for clean_number in clean_numbers:
        total += len(clean_number)
    return total


if __name__ == '__main__':
    print(count())
