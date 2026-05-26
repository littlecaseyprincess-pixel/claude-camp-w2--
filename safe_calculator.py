def main():
    while True:
        text = input("请输入算式，或输入 quit 退出：")
        if text == "quit":
            print("已退出")
            break

        parts = text.split()
        if len(parts) != 3:
            print("格式错误，请输入：数字 运算符 数字")
            continue

        try:
            left = float(parts[0])
            operator = parts[1]
            right = float(parts[2])
        except ValueError:
            print("数字无效")
            continue

        if operator == "+":
            result = left + right
        elif operator == "-":
            result = left - right
        elif operator in ("*", "×"):
            result = left * right
        elif operator in ("/", "÷"):
            if right == 0:
                print("除数不能为 0")
                continue
            result = left / right
        else:
            print("不支持的运算符")
            continue

        print("结果：", result)


if __name__ == "__main__":
    main()
