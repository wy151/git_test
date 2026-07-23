def say_hello(name):
    return f"Hello {name}"


if __name__ == "__main__":
    username = input("请输入用户名:")

    print(say_hello(username))
