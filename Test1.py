# 添加第一个方法
def sum_from_1_to_100_with_loop():
    total = 0
    for i in range(1, 101):
        total += i
    return total


result = sum_from_1_to_100_with_loop()
print(result)  # 输出5050
