# omikuji app
#
import random

omikuji = ["大吉", "吉", "小吉", "中吉", "凶"]

# print(len(omikuji))
# index = random.randint(0, len(omikuji)-1)
# result = omikuji[index]
result = random.choice(omikuji)

# print(result)
print(f"今日の運勢は．．． {result}")
