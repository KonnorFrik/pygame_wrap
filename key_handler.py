class Handler:
    def register(self, key, func, *args, **kwargs):
        """Bind a key with func for call with passed *args and **kwargs"""
        ...

    def __call__(self, pressed_keys: list):
        """Call func if pressed registered key"""
        ...


class SimpleHandler(Handler):
    def __init__(self):
        self.keys = dict()
        self.func_kwargs = dict()

    def register(self, key, func, **kw):
        if key not in self.keys:
            self.keys[key] = list()

        self.keys[key].append(func)
        self.func_kwargs[(key, func)] = kw

    def __call__(self, pressed_keys: list):
        for key, value in self.keys.items():
            if pressed_keys[key]:

                try:
                    for func in self.keys[key]:
                        func(**self.func_kwargs[(key, func)])

                except KeyError:
                    print("ERR")
                    continue
