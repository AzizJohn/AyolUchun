import random


def random_username_generator(name):
    while len(name) < 5:
        name += str(random.randint(0, 9))
    name += str(random.randint(0, 9))

    return name


def random_phone_generator():
    operators = ['99', '90', '33', '93', '94', '88']
    temp_phone = '+998'
    temp_phone += random.choice(operators)
    temp_phone += ''.join(str(random.randint(0, 9)) for _ in range(7))

    return temp_phone


def random_code_generator():
    code = "".join([str(random.randint(0, 100) % 10) for _ in range(6)])
    return code


if __name__ == '__main__':
    print(random_phone_generator())
