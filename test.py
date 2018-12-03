import math

num = int(input())
value = []
for i in range(num):
    value.append(input().split(" "))


def get_factorial(a, b):
    return math.factorial(max(a, b))


for i in value:
    a = int(i[0])
    b = int(i[1])
    n = int(i[2])
    tag = 0  # 0表示A操作，1表示B操作
    while True:
        if get_factorial(a, b) >= n:
            if tag % 2 == 0:
                print('A')
                break
            else:
                print('B')
                break
        else:
            tag += 1
            le = get_factorial(a + 1, b)
            ri = get_factorial(a, b + 1)
            if le < n and ri < n:
                if le > ri:
                    a += 1
                else:
                    b += 1
            elif le < n and ri >= n:
                a += 1
            elif le >= n and ri < n:
                b += 1
            else:
                if tag % 2 == 0:
                    print('A')
                else:
                    print('B')
                break  # 这一轮结束了