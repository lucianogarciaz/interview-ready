
class MyHashMap:
    def __init__(self):
        self.nro_keys = 100000
        self.keys = [[] for _ in range(self.nro_keys)]

    def put(self, key: int, value: int) -> None:
        hot_key = key % self.nro_keys
        for i, (stored_key, val) in enumerate(self.keys[hot_key]):
            if stored_key == key:
                self.keys[hot_key][i] = (key, value)
                return
        self.keys[hot_key].append((key, value))

                
    def get(self, key: int) -> int:
        hot_key = key % self.nro_keys
        for stored_key, val in self.keys[hot_key]:
            if key == stored_key:
                return val
        return -1
    
    def remove(self, key: int) -> None:
        hot_key = key % self.nro_keys
        for i, (stored_key, _) in enumerate(self.keys[hot_key]):
            if key == stored_key:
                del self.keys[hot_key][i]
                return


def test_basic_operations():
    hm = MyHashMap()
    hm.put(1, 1)
    hm.put(2, 2)
    assert hm.get(1) == 1
    assert hm.get(2) == 2
    assert hm.get(3) == -1
    print("✓ Basic operations passed")


def test_update_value():
    hm = MyHashMap()
    hm.put(1, 1)
    assert hm.get(1) == 1
    hm.put(1, 100)
    assert hm.get(1) == 100
    print("✓ Update value passed")


def test_remove():
    hm = MyHashMap()
    hm.put(1, 1)
    hm.put(2, 2)
    assert hm.get(1) == 1
    hm.remove(1)
    assert hm.get(1) == -1
    assert hm.get(2) == 2
    print("✓ Remove passed")


def test_remove_nonexistent():
    hm = MyHashMap()
    hm.put(1, 1)
    hm.remove(2)
    assert hm.get(1) == 1
    print("✓ Remove non-existent key passed")


def test_hash_collision():
    hm = MyHashMap()
    key1 = 1
    key2 = 1 + hm.nro_keys
    hm.put(key1, 100)
    hm.put(key2, 200)
    assert hm.get(key1) == 100
    assert hm.get(key2) == 200
    hm.remove(key1)
    assert hm.get(key1) == -1
    assert hm.get(key2) == 200
    print("✓ Hash collision passed")


def test_multiple_operations():
    hm = MyHashMap()
    hm.put(1, 1)
    hm.put(2, 2)
    assert hm.get(1) == 1
    assert hm.get(3) == -1
    hm.put(2, 1)
    assert hm.get(2) == 1
    hm.remove(2)
    assert hm.get(2) == -1
    print("✓ Multiple operations passed")


def test_large_keys():
    hm = MyHashMap()
    hm.put(1000000, 42)
    assert hm.get(1000000) == 42
    hm.put(999999, 99)
    assert hm.get(999999) == 99
    hm.remove(1000000)
    assert hm.get(1000000) == -1
    print("✓ Large keys passed")


def test_empty_hashmap():
    hm = MyHashMap()
    assert hm.get(1) == -1
    assert hm.get(0) == -1
    hm.remove(1)
    assert hm.get(1) == -1
    print("✓ Empty hashmap passed")


if __name__ == "__main__":
    test_basic_operations()
    test_update_value()
    test_remove()
    test_remove_nonexistent()
    test_hash_collision()
    test_multiple_operations()
    test_large_keys()
    test_empty_hashmap()
    print("\n✅ All tests passed!")
