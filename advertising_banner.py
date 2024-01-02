def main():
    phrases = input()
    cost = input()
    if cost == '-':
        return len(phrases) * 60
    return len(phrases) * int(cost)


if __name__ == '__main__':
    print(main())
