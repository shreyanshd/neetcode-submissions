class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.store[key]
        l = 0
        r = len(values)-1
        result = ""
        while l <= r:
            m = l + (r - l) // 2
            t, value = values[m]
            if t > timestamp:
                r = m - 1
            else:
                result = value
                l = m + 1
        return result
