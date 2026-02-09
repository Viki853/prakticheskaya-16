line = input()
word = set(line.split())
print(f'Количество: {len(word)}')
print(f'Слова: ',' '.join(sorted(word)))