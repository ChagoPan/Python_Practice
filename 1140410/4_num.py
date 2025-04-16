# 數字用法
print(-77.05)
print(79-77)
print(8*5)
print(8/5)
# 整數除法  取整數
print(8//5)
# 取餘數
print(8%5)

a = 8
print(a*5)
# 變成字串
# 字串跟數字不能用 + 符號  要先用str()轉字串
print("今年" + str(a) + "歲")

b = -8
print(b)
# 絕對值
print(abs(b))

# 次方  pow(3, 3次方)
print(pow(3, 3))

# 找到最大 / 小
print(max(2, 5, 8, 10, 1354, 20*200))
print(min(-2, 5, 8, 10, 1354, 20*200))

# 取四捨五入 (到整數)
print(round(4.45))

# 引入模組
from math import *
# 無條件捨去
print(floor(4.45))
# 無條件進入
print(ceil(4.45))
# 開根號
print(sqrt(25))