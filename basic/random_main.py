import random
import random_model
print(random_model.pi)

from random_model import pi
print(pi)

# 範圍1~10 整數
randomInt = random.randint(1, 10)
print(randomInt)

# 範圍0~1 浮點數
randomFloat = random.random()
print(randomFloat)

# 從list中隨機選取一個
list = [1, 6, 9, 2, 3]
item = random.choice(list)
print(item)

# 將list順序打亂，重新排序
list_random = [1, 2, 3, 4, 5]
random.shuffle(list_random)
print(list_random)
