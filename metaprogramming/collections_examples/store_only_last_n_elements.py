from collections import deque

if __name__ == '__main__':
    d = deque(maxlen=3)
    d.append(1)
    d.append(2)
    d.append(3)

    assert list(d) == [1, 2, 3]

    d.append(4)
    assert list(d) == [2, 3, 4]  # first should be removed
