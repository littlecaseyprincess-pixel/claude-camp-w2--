import json
FILE_NAME = "todos.json"
def load_todos():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
def save_todos(todos):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(todos, file, ensure_ascii=False, indent=2)
def show_todos(todos):
    if not todos:
        print("暂无待办")
    for index, todo in enumerate(todos, start=1):
        status = "✓" if todo["done"] else " "
        print(f"{index}. [{status}] {todo['title']}")
def add_todo(todos):
    title = input("请输入待办事项：").strip()
    if title:
        todos.append({"title": title, "done": False})
        save_todos(todos)
        print("添加成功")
def complete_todo(todos):
    show_todos(todos)
    try:
        number = int(input("请输入完成的编号："))
        if not 1 <= number <= len(todos):
            raise IndexError
        todos[number - 1]["done"] = True
        save_todos(todos)
        print("已完成")
    except (ValueError, IndexError):
        print("编号无效")
def main():
    todos = load_todos()
    while True:
        print("\n1. 查看待办\n2. 添加待办\n3. 完成待办\n4. 退出")
        choice = input("请选择：")
        if choice == "1": show_todos(todos)
        elif choice == "2": add_todo(todos)
        elif choice == "3": complete_todo(todos)
        elif choice == "4": break
        else:
            print("无效选择")
if __name__ == "__main__":
    main()
