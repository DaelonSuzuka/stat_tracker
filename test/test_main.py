from stat_tracker import StatTracker
from time import sleep


def test_main():
    stats = StatTracker()

    with stats.time1:
        sleep(0.05)

    assert repr(stats.time1) == '0.05'

    for _ in range(5):
        stats.value1 += 1

    assert stats.value1 == 5
    assert repr(stats.value1) == '5'

    for i in stats.loop1.count(range(10)):
        pass

    assert stats.loop1 == 10
    assert repr(stats.loop1) == '10'

    for i in stats('loop2').count(range(20)):
        pass

    assert stats.loop2 == 20
    assert repr(stats.loop2) == '20'
