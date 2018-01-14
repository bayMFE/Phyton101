
#Bu Kod Yapısı sayesinde daha kolay foksiyonlarla işlemler gerçekleştirilebilir.


def func1():

    print("1.")


def func2():
    print("2.")

funcmap = {1 : func1, 2 : func2}

def somefunc(a):
    funcmap[a]()

a= int(input(">>>>>"))

somefunc(a)