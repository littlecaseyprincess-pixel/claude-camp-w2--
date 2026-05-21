students = {}

while True:
    print("学员花名册管理器")
    print("1. 添加学员")
    print("2. 查询学员")
    print("3. 删除学员")
    print("4. 退出")

    choice = input("请选择操作：")

    if choice == "4":
        print("已退出")
        break

    elif choice == "1":
        name = input("请输入姓名：")
        phone = input("请输入联系方式：")
        signup_time = input("请输入报名时间：")

        if name == "":
            print("姓名不能为空")
        else:
            students[name] = {
                "phone": phone,
                "signup_time": signup_time
            }
            print("添加成功")

    elif choice == "2":
        name = input("请输入要查询的姓名：")

        if name in students:
            print(f"姓名：{name}")
            print(f"联系方式：{students[name]['phone']}")
            print(f"报名时间：{students[name]['signup_time']}")
        else:
            print("未找到该学员")

    elif choice == "3":
        name = input("请输入要删除的姓名：")

        if name in students:
            del students[name]
            print("删除成功")
        else:
            print("未找到该学员")

    else:
        print("输入错误，请重新选择 1、2、3 或 4")
    