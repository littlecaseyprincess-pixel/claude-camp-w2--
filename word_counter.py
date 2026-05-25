text = input("请输入一段英文文字：")

if text == "":
    print("输入不能为空")
    exit()
    
text = text.lower()
words = text.split()

word_counts = {}

for word in words:
    if word in word_counts:
        word_counts[word] = word_counts[word] + 1
    else:
        word_counts[word] = 1

sorted_words = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

print("词频统计结果：")

for word, count in sorted_words:
    print(f"{word}: {count}")
