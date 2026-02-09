allowed = set(input('Введите список разрешенных ID: ').split())
incoming = input('Введите список входящих ID: ').split()
for i in incoming:
    if i in allowed:
        print('OK')
    else:
        print('ADDED')
        allowed.add(i)
