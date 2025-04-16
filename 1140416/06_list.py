# 列表list、列表的用法
# score1 = 90
# score2 = 75
# ... (傳統作法)

scores = [90, 75, 60, 50, 80, 76, 75]
friends = ["黃", "白", "黑", "綠"]
things = [90, "黃", True]
phrase = "Hello Chago"
# 取得所有值
print(scores)
# 取得單一值
print(scores[0])
# 從[1]開始 取到 [i-1] 位
print(scores[1:5])
# 取[2]後所有值 (包含[2])
print(scores[2:])
# 取[3]前所有值 (不包含[3])
print(scores[:3])
# 取字串中的特定字樣
print(phrase[:5])

# 改矩陣內的值
scores[0] = 100
print(scores)

# 取得多值
# 傳統方法
# print(scores + friends)

# 方法 2 (extend: 延伸)
# scores.extend(friends)

# 方法 3 (append: 增加值) (增加多值會變成巢狀結構)
# scores.append(friends)

# 方法 4 (insert(從[2], 插入friends): 從特定位置插入)
# scores.insert(2, friends)

# 方法 5 (remove: 刪除指定的值)
# scores.remove(75)

# 方法 6 (clear: 清空所有值)
# scores.clear()

# 方法 7 (pop: 移除最後一位值)
# scores.pop()

# 方法 8 (sort: 升冪排列)
# scores.sort()

# 方法 9 (reverse: 反轉排列(前後交換))
# scores.reverse()

# print(scores)

# 方法 9 (index: 找去該值的索引值)
# if 該值有重複, 則會回傳第一次找到之索引值
# print(scores.index(75))

# 方法 10 (count: 計算該值有幾個)
print(scores.count(75))

