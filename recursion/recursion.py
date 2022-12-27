# Greatest Common Divisor
def gcd(testVariable1, testVariable2):
    if testVariable1 == testVariable2:
        return testVariable1

    if testVariable1 > testVariable2:
        return gcd(testVariable1 - testVariable2, testVariable2)
    else:
        return gcd(testVariable1, testVariable2 - testVariable1)


# Pascals Triangle
def print_pascal(testVariable):
    if testVariable == 0:
        return [1]
    else:
        pascals_triangle = [1]
        prev = print_pascal(testVariable - 1)
        for i in range(len(prev) - 1):
            pascals_triangle.append(prev[i] + prev[i + 1])

        pascals_triangle += [1]
        return pascals_triangle
