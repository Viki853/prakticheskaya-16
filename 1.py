line = input('Введите строку слов (через пробел): ')
word = set(line.split())
print(f'Количество: {len(word)}')

print(f'Слова: ',' '.join(sorted(word)))
