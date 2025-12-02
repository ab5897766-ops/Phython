# 39
def print_odds(n):
    for i in range(n + 1):
        if i % 2 == 1:
            print(i)
num = int(input())
print_odds(num)

# 40
def print_multiples_of_3(n):
    if n % 3 == 0:
        print(n)
num = int(input())
print_multiples_of_3(num)

# 41
def max_min(a, b, c, d):
    return max(a, b, c, d), min(a, b, c, d)
scores = [int(input()) for _ in range(4)]
maximum, minimum = max_min(*scores)
print(maximum, minimum)

# 42
def print_odds(n):
    for i in range(n + 1):
        if i % 2 == 1:
            print(i)
num = int(input())
print_odds(num)

# 43
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
num = int(input())
print(factorial(num))

# 44
def sum_products_over_30(i, j):
    total = 0
    for x in range(1, i + 1):
        for y in range(1, j + 1):
            if x * y >= 30:
                total += x * y
    return total
i = int(input())
j = int(input())
print(sum_products_over_30(i, j))

# 45
def sum_list(lst):
    return sum(lst)
a = [1, 2, 3, 4, 5]
print(sum_list(a))