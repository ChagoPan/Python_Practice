# \n 換行
print("Hello \nChago")

# Hello" Chago
print("Hello\" Chago")

print("Hello" + "Chago")


Hello = "Hello "
print(Hello + "Chago")

# 函式 function
Hello = "Hello Chago"
# 字母都變小寫
print(Hello.lower())
# 字母都變大寫
print(Hello.upper())
# 判斷內容是否為大寫
print(Hello.isupper())
Hello = "HELLO CHAGO"
print(Hello.isupper())
# Hello = "HELLO CHAGO"
# print(Hello.islower())
# Hello = "hello chago"
# print(Hello.islower())

# 進階
print(Hello.lower().islower())

# 數字由 0 開始計算 (結果是 E )
# 連空格也算一位
print(Hello[1])
print(Hello.index("H"))

# 替換所有包括 .replace("找到字", "換成的字")
print(Hello.replace("H", "h"))
print(Hello.replace("L", "l"))
