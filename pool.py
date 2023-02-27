class Pool:
    def add(self, object_):
        """Add object to pool for refresh"""
        ...

    def remove(self, object_):
        """Remove object from pool"""
        ...

    def refresh(self):
        """Call refresh for every object in pool"""
        ...

    def __len__(self):
        """Return count of objects in"""
        ...


class ListPool(Pool):
    """A simple pool based on list for objects BaseObject
        or with refresh method"""

    def __init__(self):
        self.objects = list()

    def add(self, object_):
        self.objects.append(object_)

    def remove(self, object_):
        del self.objects[self.objects.index(object_)]

    def refresh(self):
        for obj in self.objects:
            obj.refresh()

    def __len__(self):
        return len(self.objects)
# make dict based pool
