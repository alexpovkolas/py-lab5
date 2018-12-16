import abc


class BoundedMeta(type):
    instances_left = 1

    def __new__(mcs, name, bases, attrs, **kwargs):
        BoundedMeta.instances_left = kwargs.get('max_instance_count', 1)
        return super().__new__(mcs, name, bases, attrs)

    def __call__(cls):
        if BoundedMeta.instances_left > 0:
            BoundedMeta.instances_left -= 1
        else:
            raise TypeError
        return super().__call__()


class BoundedBase(object):
    _instances_counts = 0

    def __init__(self):
        if self.get_max_instance_count() is None:
            return
        if self.get_max_instance_count() <= BoundedBase._instances_counts:
            raise TypeError
        else:
            BoundedBase._instances_counts += 1

    @abc.abstractmethod
    def get_max_instance_count(self):
        return


