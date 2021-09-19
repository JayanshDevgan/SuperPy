class SuperPy:
    def type(var):
        return str(type(var)).split("'", 2)[1]

    def For(val, start, end):
        for val in range(start, end + 1):
            print("value of i: ", val)
