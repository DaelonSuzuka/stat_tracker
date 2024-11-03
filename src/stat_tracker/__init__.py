from time import time
from collections import defaultdict


class TimerStat:
    def __init__(self):
        super().__init__()
        self._active = False
        self._start_time = time()
        self._end_time = None
        self._lap_time = None

    def start(self):
        self._active = True
        self._start_time = time()

    def stop(self):
        self._active = False
        self._end_time = time()

    def lap(self):
        pass

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *_):
        self.stop()


class ValueStat:
    def __init__(self):
        super().__init__()
        self._value = 0

    def __iadd__(self, other):
        self._value += other
        return self

    def __isub__(self, other):
        self._value -= other
        return self


class CountStat:
    def __init__(self):
        super().__init__()
        self._count = None

    def count(self, iterable):
        self._count = 0
        for elem in iterable:
            yield elem
            self._count += 1


class Stat(TimerStat, ValueStat, CountStat):
    def __repr__(self):
        if self._count is not None:
            return f'{self._count}'
        if self._value:
            return f'{self._value}'
        if self._end_time:
            return f'{self._end_time - self._start_time:.2f}'
        return f'{''}'

    def __eq__(self, other):
        if self._count is not None:
            return self._count == other
        if self._value:
            return self._value == other


class StatTracker:
    """A StatTracker collection object"""

    def __init__(self):
        self._records = defaultdict(Stat)

    def __getattr__(self, name: str) -> Stat:
        return self._records[name]

    def __call__(self, name: str) -> Stat:
        return self._records[name]
