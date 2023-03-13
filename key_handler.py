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
                    continue


class EventKeyHandler(Handler):
    def __init__(self):
        self.keys = dict()
        self.func_kwargs = dict()

    def register(self, event_type, key, func, **kw):
        if key not in self.keys:
            self.keys[(event_type, key)] = list()

        self.keys[(event_type, key)].append(func)
        self.func_kwargs[(event_type, key, func)] = kw
        #print(self.keys)
        #print(self.func_kwargs)

    def __call__(self, all_events: list):
        for event in all_events:

            if event.type in [obj[0] for obj in self.keys.keys()]:
                try:
                    for func in self.keys[(event.type, event.key)]:
                        func(**self.func_kwargs[(event.type, event.key, func)])

                except Exception:
                    pass


class MultiHandler(Handler):
    def __init__(self):
        self.keys = dict()
        self.event_keys = dict()

        self.func_kwargs = dict()
        self.event_func_kwargs = dict()

        self.mode_once = "once"
        self.mode_pressed = "pressed"


    def _register_key(self, key, func, **kw):
        if key not in self.keys:
            self.keys[key] = list()

        self.keys[key].append(func)
        self.func_kwargs[(key, func)] = kw
        #print("keys", self.keys)


    def _register_event(self, event_type, key, func, **kw):
        if key not in [obj[1] for obj in self.event_keys.keys()]:
            self.event_keys[(event_type, key)] = list()

        self.event_keys[(event_type, key)].append(func)

        self.event_func_kwargs[(event_type, key, func)] = kw
        #print("event keys", self.event_keys)


    def register(self, mode: str, key, func, event_type = None, **kw):
        if mode == self.mode_pressed:
            self._register_key(key, func, **kw)

        elif mode == self.mode_once:
            if not event_type:
                raise Exception("Event type not passed")

            self._register_event(event_type, key, func, **kw)

        else:
            raise Exception("Unknown mode")


    def __call__(self, events: list = None, pressed_keys: list = None):
        if pressed_keys:
            for key, value in self.keys.items():
                if pressed_keys[key]:

                    try:
                        for func in self.keys[key]:
                            func(**self.func_kwargs[(key, func)])

                    except KeyError:
                        continue

        if events:
            for event in events:

                if event.type in [obj[0] for obj in self.event_keys.keys()]:
                    try:
                        for func in self.event_keys[(event.type, event.key)]:
                            func(**self.event_func_kwargs[(event.type, event.key, func)])

                    except Exception:
                        pass


if __name__ == "__main__":
    import pygame as pg
    pg.init()
    handler = MultiHandler()
    #handler.register(event_type=pg.KEYUP, key=pg.K_x, func=pg.quit)
    handler.register(mode="once", event_type=pg.KEYDOWN, key=pg.K_x, func=exit)
    handler.register(mode="pressed", key=pg.K_f, func=lambda: print("F"))
    #handler.register(mode="once", event_type=pg.KEYUP, key=pg.K_w, func=lambda: print("Up"))
    #handler.register(mode="once", key=pg.K_w, func=lambda: print("Up"))

    W = 400
    H = 400
    sc = pg.display.set_mode((W, H))
    clock = pg.time.Clock()
    while True:
        clock.tick(30)

        events = pg.event.get()
        keys = pg.key.get_pressed()
        handler(pressed_keys=keys, events=events)

        sc.fill(0)
        pg.display.flip()
