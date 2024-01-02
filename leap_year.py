def main():
    year = int(input())
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


if __name__ == '__main__':
    print(main())
