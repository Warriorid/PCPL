import random
def gen_Random(count, start, end):
    for i in range(count):
        print(random.randint(start, end))


if __name__ == '__main__':
    gen_Random(5,1,3)