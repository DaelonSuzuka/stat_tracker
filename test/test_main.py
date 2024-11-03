from stat_tracker import StatTracker
from time import sleep


def test_time():
    stats = StatTracker()

    with stats.time1:
        with stats.time2:
            sleep(0.05)
        sleep(0.05)

    assert repr(stats.time1) == '0.10'
    assert repr(stats.time2) == '0.05'


def test_value():
    stats = StatTracker()

    stats.value = 10

    assert stats.value == 10
    assert repr(stats.value) == '10'

    for _ in range(5):
        stats.value += 1

    assert stats.value == 15
    assert repr(stats.value) == '15'

    for _ in range(5):
        stats.value -= 1

    assert stats.value == 10
    assert repr(stats.value) == '10'


def test_count():
    stats = StatTracker()

    for i in stats.loop1.count(range(10)):
        pass

    assert stats.loop1 == 10
    assert repr(stats.loop1) == '10'

    for i in stats('loop2').count(range(20)):
        pass

    assert stats.loop2 == 20
    assert repr(stats.loop2) == '20'


def test_list():
    stats = StatTracker()

    stats.tags.append('a')
    stats.tags.extend(['b', 'c'])

    assert 'a' in stats.tags
    assert 'b' in stats.tags
    assert 'c' in stats.tags
    assert repr(stats.tags) == "['a', 'b', 'c']"

    stats.list.append(5)
    stats.list.append(10)
    stats.list.append(15)

    assert repr(stats.list) == '[5, 10, 15]'
    assert sum(stats.list) == 30
