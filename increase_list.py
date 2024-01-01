def main():
    start_list = input().split()
    finish_list = []
    number = int(input())
    for i in range(len(start_list)):
        finish_list.append(int(start_list[i]) * number)
    return finish_list


if __name__ == '__main__':
    print(main())
