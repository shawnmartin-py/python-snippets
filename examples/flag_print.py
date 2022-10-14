class FlagPrintDecorator:
    _colors = {
        "red": "[41;1m",
        "white": "[47;1m",
        "blue": "[44;1m",
        "yellow": "[43;1m",
    }
    _reset_code = "\33[0m"
    _arrow = "  \33{color_code} ->" + _reset_code + "\33[1m"

    def __init__(self, print_func):
        self.print_func = print_func

    def __call__(self, *args, flag = False, color = "red"):
        if flag and (code := self._colors.get(color)):
            args = self._arrow.format(color_code=code), *args, self._reset_code
        self.print_func(*args)



flag_print = FlagPrintDecorator(print)


if __name__ == "__main__":
    #print = flag_print

    flag_print("text", flag=True)


    print("sadfad")






