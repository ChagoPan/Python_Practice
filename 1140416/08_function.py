# function 用 def
# 只要遇到 return 就會結束

# 設定 function
def hello(name, age): 
    print("hello " + name + ", 今年 " + str(age) + " 歲")
# 使用 function
# hello("Chago", 28)

# 數字相加
# def add(num1, num2):
    ## 使用 return 以便後續運算處理
    # return num1 + num2
# print(add(18, 25))

### 注意用法 1
# 會出現兩者值都出現
def add(num1, num2):
    print(num1 + num2)
    return 50
value = add(3, 4)
print(value)

### 注意用法 2
# 在函式沒有return 會預設出現 None
# 就像JS function 要 return 意思
def add(num1, num2):
    print(num1 + num2)

value = add(3, 4)
print(value)