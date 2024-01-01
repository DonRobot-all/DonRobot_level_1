def main():
    string_alphabet = '-абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    character = input().lower()
    return string_alphabet.index(character)


if __name__ == '__main__':
    print(main())
