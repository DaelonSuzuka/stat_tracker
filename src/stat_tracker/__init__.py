from time import time, sleep
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
    # def __init__(self):
    #     super().__init__()
    #     self._list = []

    def __repr__(self):
        if self._count is not None:
            return f'{self._count}'
        if self._value:
            return f'{self._value}'
        if self._end_time:
            return f'{self._end_time - self._start_time:.2f}'
        return f'{''}'


class StatTracker:
    """A StatTracker collection object"""

    def __init__(self):
        self._records = defaultdict(Stat)

    def __getattr__(self, name: str) -> Stat:
        return self._records[name]

    def __call__(self, name: str) -> Stat:
        return self._records[name]


if __name__ == '__main__':
    stats = StatTracker()

    with stats.time1:
        sleep(0.05)

    for _ in range(5):
        stats.value1 += 1

    for i in stats.loop1.count(range(10)):
        pass

    for i in stats('loop2').count(range(100)):
        pass

    print(f'time {stats.time1}')  # time 0.05
    print(f'added {stats.value1}')  # added 5
    print(f'counted {stats.loop1}')  # counted 10
    print(f'counted {stats('loop2')}')  # counted 100
