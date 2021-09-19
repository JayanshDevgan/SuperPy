from superpy import SuperPy


def getTypeOfVar_SuperPyFunction(var):
    return SuperPy.type(var)


def getTypeOfVar_NormalFuction(var):
    return type(var)


def forLoop_SuperPyFunction(v, s, e):
    return SuperPy.For(v, s, e)


def forLoop_NormalFunction(i):
    for i in range(0, 10):
        print("value of i: ", i)


if __name__ == "__main__":
    print(getTypeOfVar_SuperPyFunction(var="None"))
    print(getTypeOfVar_NormalFuction(var="None"))
    print(forLoop_NormalFunction(1))
    print(forLoop_SuperPyFunction(1, 0, 10))