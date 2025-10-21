#15
nums = list(map(int, input("숫자 10개를 입력하세요: ").split()))
print(min(nums))
print(max(nums))

입력받은 숫자 10개 중에서 가장 작은 값과 큰 값을 출력하기 위해 min, max를 사용했다.

#16
nums = list(map(int, input("숫자 10개를 입력하세요: ").split()))
result = sum(nums) - min(nums) - max(nums)
print(result)

전체 합에서 최솟값과 최댓값을 빼면 나머지 값들의 합이 되기 때문에 그렇게 계산했다.

#17
a = [10, 20, 30, 40, 30, 20, 10]
a = [x for x in a if x != 20]
print(a)


리스트에서 20을 모두 없애려면 20이 아닌 값만 남기면 된다

#18
nums = [x for x in range(1, 6)]
print(nums)

1부터 5까지 리스트를 만들기 위해 range(1, 6)을 그대로 리스트 컴프리헨션에 넣었다.

#19
odds = [x for x in range(1, 21) if x % 2 == 1]
print(odds)

홀수만 출력해야 하니까 x % 2 == 1 조건을 걸었다

#20
n1, n2 = map(int, input().split())
p = [2**i for i in range(n1, n2+1)]
print(p[:1] + p[2:-1])

입력받은 범위로 2의 거듭제곱 리스트를 만들고, 두 번째랑 네 번째 값을 빼고 출력한 것이다.

#21
text = input()
print(text.replace("Hello", "Hi"))

입력된 문자열에서 "Hello"를 "Hi"로 바꾸기 위해 replace()를 썼다.

#22
print("/".join(input().split()))

입력받은 문자열 4개를 공백 기준으로 나눈 뒤, /로 연결하려고 split()과 join()을 썼다.

#23
print(input().lower().rjust(10))

입력된 성을 소문자로 바꾸고, 길이 10 기준으로 오른쪽 정렬하려고 lower()와 rjust(10)을 썼다.

#24
print(sorted(map(int, input().split(";")), reverse=True))

세미콜론으로 구분된 가격들을 정수로 바꾼 뒤, 내림차순 정렬하려고 split(";"), map(int, ...), sorted(..., reverse=True)를 썼다.


