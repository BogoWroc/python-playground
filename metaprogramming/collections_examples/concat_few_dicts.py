from collections import ChainMap

if __name__ == '__main__':
    d1 = {'x': 1, 'y': 2}
    d2 = {'x': 5, 'z': 10}

    cmap = ChainMap(d1, d2)  # first key and value is used. Duplication is ignored
    assert sorted(list(cmap.keys())) == sorted(['x', 'y', 'z'])
    assert sorted(list(cmap.values())) == sorted([1, 2, 10])
