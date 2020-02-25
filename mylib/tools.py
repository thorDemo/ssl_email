from random import choice, sample


def rand_from():
    file = open('content/from.txt', 'r', encoding='utf-8')
    data = []
    for line in file:
        data.append(line.strip())
    return choice(data)


def rand_to():
    file = open('content/to.txt', 'r', encoding='utf-8')
    data = []
    for line in file:
        data.append(line.strip())
    return choice(data)


def rand_title():
    file = open('content/title_1.txt', 'r', encoding='utf-8')
    data = []
    for line in file:
        data.append(line.strip())
    return choice(data)


def rand_chars():
    str = "qwertyuiopasdfghjklzxcvbnm"
    return ''.join(sample(str, 5))


def rand_account():
    file = open('account/user.txt', 'r', encoding='utf-8')
    data = []
    for line in file:
        data.append(line.strip())
    string = str(choice(data)).split(' ')
    return string[0], string[1].strip()
