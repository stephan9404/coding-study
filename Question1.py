# 문제 : 10미만의 자연수에서 3과 5의 배수를 구하면 3,5,6,9이다.
# 이들의 총합은 23이다.
# 1000미만의 자연수에서 3,5의 배수의 총합을 구하라.

print("해답 1:")
print(sum([x for x in range(1,1001) if x % 3==0 or x % 5==0]))


print("해답 2:")
set3 = set(range(3, 1001, 3))
set5 = set(range(5, 1001, 5))
#합집합을 구하는 공식은 | 이거임
set6 = set3|set5
print(sum(set6))


print("해답 3:")
sum = 0
for x in range(1, 1001):
    if (x%3)==0 or (x%5)==0:
        sum+=x
print(sum)





