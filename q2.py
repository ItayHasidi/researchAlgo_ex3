import string

history: dict = {}


def lastcall(func):
    """
    A decorator function that remembers all previous calls, and if a call was already made the function will give
    the answer without calling the original function again.

    >>> f(10)
    100
    >>> f(10)
    I already told you that the answer is 100!
    >>> f(1)
    1
    >>> f(5)
    25
    >>> f(5)
    I already told you that the answer is 25!
    >>> f(1)
    I already told you that the answer is 1!
    >>> g("hello")
    5
    >>> g("hello")
    I already told you that the answer is 5!
    >>> g("HELLO")
    5

    """
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

@lastcall
def g(x: string):
    return len(x)



if __name__ == '__main__':
    f(2)
    f(2)
    f(20)
    f(2)
    f(20)
    f(20)
