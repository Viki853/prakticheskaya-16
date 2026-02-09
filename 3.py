server_A = set(input('Введите имена файлов сервера А: ').split())
server_B = set(input('Введите имена файлов сервера В: ').split())
common = server_A & server_B
lost = server_A - server_B
print(f'Общие файлы: {common}')
print(f'Потерянные файлы: {lost}')

