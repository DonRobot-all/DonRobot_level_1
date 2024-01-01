def main():
    numbers = input().split()
    sum_numbers = sum(map(int, numbers))
    if sum_numbers % 2 == 0:
        return 'чётное'
    return 'нечётное'


if __name__ == '__main__':
    print(main())
