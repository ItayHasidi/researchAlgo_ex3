history: dict = {}


def lastcall(func):
    def wrap(*args, **kwargs):
        for val in args:
            if val in history.keys():
                print("I already told you that the answer is {}!".format(history[val]))
            else:
                history[val] = func(val)
                print(history[val])
        for val in kwargs:
            if val in history.keys():
                print("I already told you that the answer is {}!".format(history[val]))
            else:
                history[val] = func(val)
                print(history[val])
    return wrap


@lastcall
def f(x: int):
    return x ** 2


if __name__ == '__main__':
    f(2)
    f(2)
    f(20)
    f(2)
    f(20)
    f(20)