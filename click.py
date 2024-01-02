def main():
    words = input().split()
    new_list = []
    flag = True
    for word in words:
        if word.lower() == 'flick':
            flag = not flag
        new_list.append(flag)
    return new_list


if __name__ == '__main__':
    print(main())
