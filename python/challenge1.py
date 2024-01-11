# Challenge 1

units = [
    'zero', 'one',
    'two', 'three', 'four',
    'five', 'six', 'seven',
    'eight', 'nine', 'ten',
    'eleven', 'twelve', 'thirteen',
    'fourteen', 'fifteen', 'sixteen',
    'seventeen', 'eighteen', 'nineteen',
]

tens = [
    'twenty', 'thirty', 'forty',
    'fifty', 'sixty', 'seventy',
    'eighty', 'ninety',
]

scales = ['hundred', 'thousand', 'million', ]


def convert_str_to_int(string_value):
    string_list = string_value.split()  # splitting key words up
    values_map = {}  # for assiging each value a scale
    # assigning units and tens with scales of 1
    for i, num in enumerate(units):
        values_map[num] = (1, i)
    for i, num in enumerate(tens):
        scale, increment = (1, i * 10)
        values_map[num] = (scale, scale * 20 + increment)
    for i, num in enumerate(scales):
        # hundreds and greater are not incremented but used as scales
        values_map[num] = (10 ** (i * 3 or 2), 0)

    # print(values_map)
    integer = result = 0  # tracking current value and result
    for i, string in enumerate(string_list):
        if string != 'negative':    # skipping - if it exists in string
            scale, increment = values_map[string]
            integer = integer * scale + increment
            if scale >= 1000:
                result += integer
                integer = 0
    # ensuring negative values are calculated
    if string_list[0] == 'negative':
        return -abs(result) + -abs(integer)
    return result + integer


print(convert_str_to_int("negative seven hundred twenty nine"))
print(convert_str_to_int("six"))
print(convert_str_to_int("one million one hundred one"))
print(convert_str_to_int(
    "negative nine hundred ninety nine thousand nine hundred ninety nine"))
