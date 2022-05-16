log = input()
paswrd = input()
user(log, paswrd)
def user(log, paswrd):
    with open('users.txt', 'w') as f:
        f.write(f'{log}:{paswrd}')
