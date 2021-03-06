import copy

class BaseHIObj:
    _OWNER = "WhiteBlackGoose"
    _PROJECT_NAME = "HI-19"
    _VERSION = "2.0.1"


class BaseConfig(BaseHIObj):
    def __str__(self):
        r = ""
        for s in [x for x in dir(self)]:
            if s[:1] != "_":
                r += (s + " = " + str(eval("self." + s))) + "\n"
        return r

    def copy(self):
        return copy.copy(self)

    def _ipython_display_(self):
        print(str(self))

