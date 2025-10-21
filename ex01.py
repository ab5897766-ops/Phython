# === 15
nums = list(map(int, input("숫자 10개를 입력하세요: ").split()))
print(min(nums))
print(max(nums))

# === 16
nums = list(map(int, input("숫자 10개를 입력하세요: ").split()))
result = sum(nums) - min(nums) - max(nums)
print(result)

# === 17
a = [10, 20, 30, 40, 30, 20, 10]
a = [x for x in a if x != 20]
print(a)

# === 18 
nums = [x for x in range(1, 6)]
print(nums)

# === 19
odds = [x for x in range(1, 21) if x % 2 == 1]
print(odds)

# === 20
n1, n2 = map(int, input().split())
p = [2**i for i in range(n1, n2+1)]
print(p[:1] + p[2:-1])

# === 21
text = input()
print(text.replace("Hello", "Hi"))

# === 22
print("/".join(input().split()))

# === 23
print(input().lower().rjust(10))

# === 24
print(sorted(map(int, input().split(";")), reverse=True))